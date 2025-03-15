import psycopg2
from app.models.support_message_model import SupportMessageModel

class SupportMessagePostgresRepository:
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

    def get_support_message(self, message_id: int) -> SupportMessageModel:
        '''
        Retrieves a support message from the PostgreSQL database by its ID.
        Args:
            message_id (int): The ID of the support message to retrieve.
        Returns:
            SupportMessageModel: The retrieved support message.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the support message from the PostgreSQL database.
        '''
        try:
            query = "SELECT * FROM Support WHERE id = %s;"
            with self.__connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (message_id,))
                    result = cursor.fetchone()
                    if result:
                        return SupportMessageModel(
                            id=result[0],
                            user_id=result[1],
                            description=result[2],
                            status=result[3],
                            subject=result[4],
                            created_at=result[5]
                        )
                    else:
                        return None
        except psycopg2.Error as e:
            raise e

    def save_support_message(self, user_id: int, description: str, status: str, subject: str):
        '''
        Saves a support message in the PostgreSQL database.
        Args:
            user_id (int): The ID of the user.
            description (str): The description of the support message.
            status (str): The status of the support message.
            subject (str): The subject of the support message.
        Returns:
            int: The ID of the saved support message.
        Raises:
            psycopg2.Error: If an error occurs while saving the support message in the PostgreSQL database.
        '''
        try:
            query = """
                INSERT INTO Support (user_id, description, status, subject, created_at)
                VALUES (%s, %s, %s::boolean, %s, NOW())
                RETURNING id;
            """
            with self.__connect() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, (user_id, description, status, subject))
                    conn.commit()
                    return cursor.fetchone()[0]
        except psycopg2.Error as e:
            conn.rollback()
            raise e