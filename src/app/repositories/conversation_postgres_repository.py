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

        
        query = "SELECT id, title FROM Conversations WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    return ConversationEntity(id=result[0], title=result[1])
                else:
                    return None
        
        
    def get_conversations(self) -> list[ConversationEntity]:
        '''
        Retrieves all conversations from the PostgreSQL database.
        Returns:
            list[ConversationEntity]: A list of all retrieved conversations.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the conversations from the PostgreSQL database.
        '''
        
        query = "SELECT id, title FROM Conversations;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return [ConversationEntity(id=row[0], title=row[1]) for row in results]

    def save_conversation_title(self, conversation: ConversationEntity) -> int:
        '''
        Saves the title of a conversation in the PostgreSQL database.
        If the conversation does not exist, it creates a new one.
        Args:
            conversation_entity (ConversationEntity): The conversation entity containing the ID and title.
        Returns:
            bool: True if the operation is successful, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while saving the conversation title in the PostgreSQL database.
        '''
        
        insert_query = "INSERT INTO Conversations (title) VALUES (%s)"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(insert_query, (conversation.get_title(),))
                conn.commit()
                return True