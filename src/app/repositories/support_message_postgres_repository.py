import psycopg2
from entities.support_message_entity import SupportMessageEntity

class SupportMessagePostgresRepository:
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

    def get_support_message(self, support_message: SupportMessageEntity) -> SupportMessageEntity:
        '''
        Retrieves a support message from the PostgreSQL database by its entity.
        Args:
            support_message (SupportMessageEntity): The support message entity containing the ID to retrieve.
        Returns:
            SupportMessageEntity: The retrieved support message, or None if not found.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the support message from the PostgreSQL database.
        '''
        query = "SELECT * FROM Support WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (support_message.get_id(),))
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
            list[SupportMessageEntity]: A list of all retrieved support messages.
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
        

    def save_support_message(self, support_message: SupportMessageEntity) -> int:
        '''
        Saves a support message in the PostgreSQL database.
        Args:
            SupportMessageEntity (SupportMessageEntity): The support message entity to save.
        Returns:
            int: The ID of the saved support message.
        Raises:
            psycopg2.Error: If an error occurs while saving the support message in the PostgreSQL database.
        '''
        
        query = """
            INSERT INTO Support (user_id, description, status, subject, created_at)
            VALUES (%s, %s, %s::boolean, %s, %s)
            RETURNING id;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (support_message.get_user_id(), support_message.get_description(), support_message.get_status(), support_message.get_subject(), support_message.get_created_at() ))
                conn.commit()
                return cursor.fetchone()[0]
            
    def delete_support_message(self, support_message : SupportMessageEntity)-> bool:
        '''
        Deletes a support message from the PostgreSQL database by its ID.
        Args:
            support_message (SupportMessageEntity): The support message entity to delete.
        Returns:
            bool: True if the support message was successfully deleted, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while deleting the support message from the PostgreSQL database.
        '''
        query = "DELETE FROM Support WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (support_message.get_id(),))
                conn.commit()
                return cursor.rowcount > 0
        