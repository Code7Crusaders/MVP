import psycopg2
from entities.message_entity import MessageEntity

class MessagePostgresRepository:
    def __init__(self, db_config: dict):
        '''
        Initializes the PostgresRepository with the given database configuration.
        Args:
            db_config (dict): The configuration dictionary for the PostgreSQL database.
        '''
        self.__conn = psycopg2.connect(**db_config)

    def get_message(self, message_id: int) -> MessageEntity:
        '''
        Retrieves a message from the PostgreSQL database by its ID.
        Args:
            message_id (int): The ID of the message to retrieve.
        Returns:
            MessageEntity: The retrieved message data.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the message from the PostgreSQL database.
        '''
        try:
            select_message_query = """
            SELECT id, text, created_at, user_id, conversation_id, rating
            FROM Messages
            WHERE id = %s;
            """
            with self.__conn.cursor() as cursor:
                cursor.execute(select_message_query, (message_id,))
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
                    print(f"No message found with ID {message_id}")
                    return None
        except psycopg2.Error as e:
            print(f"A connection error occurred while retrieving the message from the Postgres database: {e}")
            self.__conn.rollback()
            return None
        except Exception as e:
            print(f"An error occurred while retrieving the message from the Postgres database: {e}")
            self.__conn.rollback()
            return None
        
    def get_messages_by_conversation(self, conversation_id: int) -> list[MessageEntity]:
        '''
        Retrieves all messages associated with a specific conversation from the PostgreSQL database.
        Args:
            conversation_id (int): The ID of the conversation.
        Returns:
            list[MessageEntity]: A list of MessageEntity objects.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the messages from the PostgreSQL database.
        '''
        try:
            select_messages_query = """
            SELECT id, text, created_at, user_id, conversation_id, rating
            FROM Messages
            WHERE conversation_id = %s;
            """
            with self.__conn.cursor() as cursor:
                cursor.execute(select_messages_query, (conversation_id,))
                rows = cursor.fetchall()
                return [MessageEntity(id=row[0], text=row[1], created_at=row[2], user_id=row[3], conversation_id=row[4], rating=row[5]) for row in rows]
        except psycopg2.Error as e:
            print(f"An error occurred while retrieving the messages from the PostgreSQL database: {e}")
            self.__conn.rollback()
            return []
        except Exception as e:
            print(f"An error occurred while retrieving the messages from the PostgreSQL database: {e}")
            self.__conn.rollback()
            return []
    
    def save_message(self, message: MessageEntity):
        '''
        Saves a message into the PostgreSQL database.
        Args:
            message (MessageEntity): The message data to be saved.
        Raises:
            psycopg2.Error: If an error occurs while saving the message in the PostgreSQL database.
        '''
        try:
            insert_message_query = """
            INSERT INTO Messages (text, created_at, user_id, conversation_id, rating)
            VALUES (%s, %s, %s, %s, %s);
            """
            params = (message.text, message.created_at, message.user_id, message.conversation_id, message.rating)
            with self.__conn.cursor() as cursor:
                cursor.execute(insert_message_query, params)
            self.__conn.commit()
            print("Message saved successfully in the Postgres database.")
        except psycopg2.Error as e:
            print(f"A connection error occurred while saving the message in the Postgres database: {e}")
            self.__conn.rollback()
        except Exception as e:
            print(f"An error occurred while saving the message in the Postgres database: {e}")
            self.__conn.rollback()

