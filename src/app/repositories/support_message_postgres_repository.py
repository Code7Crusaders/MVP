import psycopg2
from entities.support_message_entity import SupportMessageEntity

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

    def get_support_message(self, message_id: int) -> SupportMessageEntity:
        '''
        Retrieves a support message from the PostgreSQL database by its ID.
        Args:
            message_id (int): The ID of the support message to retrieve.
        Returns:
            SupportMessageEntity: The retrieved support message.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the support message from the PostgreSQL database.
        '''
        
        query = "SELECT * FROM Support WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (message_id,))
                result = cursor.fetchone()
                if result:
                    return SupportMessageEntity(
                        id=result[0],
                        user_id=result[1],
                        description=result[2],
                        status=result[3],
                        subject=result[4],
                        created_at=result[5]
                    )
                else:
                    return None

    def get_support_messages(self) -> list[SupportMessageEntity]:
        '''
        Retrieves all support messages from the PostgreSQL database.
        Returns:
            list[SupportMessageEntity]: A list of support messages.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the support messages from the PostgreSQL database.
        '''
        
        query = "SELECT * FROM Support;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return [
                    SupportMessageEntity(
                        id=row[0],
                        user_id=row[1],
                        description=row[2],
                        status=row[3],
                        subject=row[4],
                        created_at=row[5]
                    )
                    for row in results
                ]
        

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
            
    def delete_support_message(self, message_id: int)-> bool:
        '''
        Deletes a support message from the PostgreSQL database by its ID.
        Args:
            message_id (int): The ID of the support message to delete.
        Raises:
            psycopg2.Error: If an error occurs while deleting the support message from the PostgreSQL database.
        '''
        
        query = "DELETE FROM Support WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (message_id,))
                conn.commit()
                return cursor.rowcount > 0
        