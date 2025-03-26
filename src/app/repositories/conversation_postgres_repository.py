import psycopg2
from entities.conversation_entity import ConversationEntity

class ConversationPostgresRepository:
    def __init__(self, db_config: dict):
        '''
        Initializes the PostgresRepository with the given database configuration.
        Args:
            db_config (dict): The configuration dictionary for the PostgreSQL database.
        '''
        self.__db_config = db_config

    def __connect(self):
        '''
        Establishes a new connection to the PostgreSQL database.
        Returns:
            psycopg2.extensions.connection: The connection object to the PostgreSQL database.
        '''
        return psycopg2.connect(**self.__db_config)

    def get_conversation(self, conversation: ConversationEntity) -> ConversationEntity:
        '''
        Retrieves a conversation from the PostgreSQL database by its ID.
        Args:
            conversation (ConversationEntity): The conversation entity containing the ID to retrieve.
        Returns:
            ConversationEntity: The retrieved conversation, or None if not found.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the conversation from the PostgreSQL database.
        '''
        id = conversation.get_id()

        query = "SELECT id, title, user_id FROM Conversations WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    return ConversationEntity(id=result[0], title=result[1], user_id=result[2])
                else:
                    return None
        
        
    def get_conversations(self, conversation: ConversationEntity) -> list[ConversationEntity]:
        '''
        Retrieves all conversations associated with a specific user from the PostgreSQL database.
        Args:
            user_id (int): The ID of the user whose conversations are to be retrieved.
        Returns:
            list[ConversationEntity]: A list of all retrieved conversations.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the conversations from the PostgreSQL database.
        '''
        
        query = """
        SELECT id, title, user_id
        FROM Conversations
        WHERE user_id = %s;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (conversation.get_user_id(),))
                results = cursor.fetchall()
                return [ConversationEntity(id=row[0], title=row[1], user_id=row[2]) for row in results]

    def save_conversation_title(self, conversation: ConversationEntity) -> int:
        '''
        Saves the title of a conversation in the PostgreSQL database.
        If the conversation does not exist, it creates a new one.
        Args:
            conversation (ConversationEntity): The conversation entity containing the user ID and title.
        Returns:
            int: The ID of the saved conversation.
        Raises:
            psycopg2.Error: If an error occurs while saving the conversation title in the PostgreSQL database.
        '''
        insert_query = """
        INSERT INTO Conversations (title, user_id) 
        VALUES (%s, %s) 
        RETURNING id;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(insert_query, (conversation.get_title(), conversation.get_user_id()))
                saved_id = cursor.fetchone()[0]
                conn.commit()
                return saved_id
            
    def delete_conversation(self, conversation: ConversationEntity)-> bool:
        '''
        Deletes a conversation from the PostgreSQL database.
        Args:
            conversation (ConversationEntity): The conversation entity to delete.
        Returns:
            bool: True if the conversation was successfully deleted, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while deleting the conversation from the PostgreSQL database.
        '''
        id = conversation.get_id()
        delete_query = "DELETE FROM Conversations WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, (id,))
                conn.commit()
                return cursor.rowcount > 0