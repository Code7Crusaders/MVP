import psycopg2
from app.models.conversation_model import ConversationModel

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

    def get_conversation(self, conversation_id: int) -> ConversationModel:
        '''
        Retrieves a conversation from the PostgreSQL database by its ID.
        Args:
            conversation_id (int): The ID of the conversation to retrieve.
        Returns:
            ConversationModel: The retrieved conversation.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the conversation from the PostgreSQL database.
        '''
        try:
            query = "SELECT id, title FROM Conversations WHERE id = %s;"
            with self.__connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (conversation_id,))
                    result = cursor.fetchone()
                    if result:
                        return ConversationModel(id=result[0], title=result[1])
                    else:
                        return None
        except psycopg2.Error as e:
            raise e

    def save_conversation_title(self, conversation_id: int, conversation_title: str):
        '''
        Saves the title of a conversation in the PostgreSQL database.
        If the conversation does not exist, it creates a new one.
        Args:
            conversation_id (int): The ID of the conversation to update or create.
            conversation_title (str): The title of the conversation.
        Raises:
            psycopg2.Error: If an error occurs while saving the conversation title in the PostgreSQL database.
        '''
        try:
            select_query = "SELECT id FROM Conversations WHERE id = %s;"
            update_query = "UPDATE Conversations SET title = %s WHERE id = %s;"
            insert_query = "INSERT INTO Conversations (id, title) VALUES (%s, %s);"
            with self.__connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(select_query, (conversation_id,))
                    result = cursor.fetchone()
                    if result:
                        cursor.execute(update_query, (conversation_title, conversation_id))
                    else:
                        cursor.execute(insert_query, (conversation_id, conversation_title))
                    conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            raise e

