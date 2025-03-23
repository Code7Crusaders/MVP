import psycopg2
from entities.message_entity import MessageEntity
from entities.conversation_entity import ConversationEntity

class MessagePostgresRepository:
    def __init__(self, db_config: dict):
        '''
        Initializes the repository with the given database configuration.
        Args:
            db_config (dict): A dictionary containing the PostgreSQL database configuration parameters.
        '''
        self.__db_config = db_config

    def __connect(self):
        '''
        Creates and returns a new connection to the PostgreSQL database.
        Returns:
            psycopg2.extensions.connection: A connection object to interact with the PostgreSQL database.
        '''
        return psycopg2.connect(**self.__db_config)

    def get_message(self, message: MessageEntity) -> MessageEntity:
        '''
        Retrieves a message from the PostgreSQL database by its ID.
        Args:
            message (MessageEntity): The message entity containing the ID of the message to retrieve.
        Returns:
            MessageEntity: The retrieved message data.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the message from the PostgreSQL database.
        '''
        
        select_message_query = """
        SELECT id, text, created_at, user_id, conversation_id, rating
        FROM Messages
        WHERE id = %s;
        """
        with self.__connect() as connection:  # Call the method to get the connection object
            with connection.cursor() as cursor:
                cursor.execute(select_message_query, (message.get_id(),))
                result = cursor.fetchone()
                if result:
                    message = MessageEntity(
                        id=result[0],
                        text=result[1],
                        created_at=result[2],
                        user_id=result[3],
                        conversation_id=result[4],
                        rating=result[5]
                    )
                    return message
                else:
                    raise ValueError(f"Message with ID {message.get_id()} not found.")
            
    def get_messages_by_conversation(self, conversation: MessageEntity) -> list[MessageEntity]:
        '''
        Retrieves all messages associated with a specific conversation from the PostgreSQL database.
        Args:
            conversation (ConversationEntity): The conversation entity containing the ID of the conversation.
        Returns:
            list[MessageEntity]: A list of MessageEntity objects.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the messages from the PostgreSQL database.
        '''
        
        select_messages_query = """
        SELECT id, text, created_at, user_id, conversation_id, rating
        FROM Messages
        WHERE conversation_id = %s;
        """
        with self.__connect() as connection:  # Call the method to get the connection object
            with connection.cursor() as cursor:
                cursor.execute(select_messages_query, (conversation.get_conversation_id(),))
                rows = cursor.fetchall()
                if rows:
                    return [
                        MessageEntity(
                            id=row[0],
                            text=row[1],
                            created_at=row[2],
                            user_id=row[3],
                            conversation_id=row[4],
                            rating=row[5]
                        ) for row in rows
                    ]
                else:
                    raise ValueError(f"No messages found for conversation ID {conversation.get_conversation_id()}.")
    
    def save_message(self, message: MessageEntity) -> int:
        '''
        Saves a message into the PostgreSQL database and returns the ID of the created message.
        Args:
            message (MessageEntity): The message data to be saved.
        Returns:
            int: The ID of the created message.
        Raises:
            psycopg2.Error: If an error occurs while saving the message in the PostgreSQL database.
        '''
        
        insert_message_query = """
        INSERT INTO Messages (text, created_at, user_id, conversation_id, rating)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
        """
        params = (message.get_text(), message.get_created_at(), message.get_user_id(), message.get_conversation_id(), message.get_rating())
        with self.__connect() as connection:  
            with connection.cursor() as cursor:
                cursor.execute(insert_message_query, params)
                created_id = cursor.fetchone()[0]
            connection.commit()
        return created_id

    def delete_message(self, message: MessageEntity) -> bool:
        '''
        Deletes a message from the PostgreSQL database.
        Args:
            message (MessageEntity): The message to be deleted.
        Returns:
            bool: True if the message was deleted successfully, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while deleting the message from the PostgreSQL database.
        '''
        
        delete_message_query = """
        DELETE FROM Messages
        WHERE id = %s;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_message_query, (message.get_id(),))
                conn.commit()
                return cursor.rowcount > 0