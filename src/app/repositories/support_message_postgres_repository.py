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
                    raise ValueError(f"No support messages found for support message ID {support_message.get_id()}.")

    def get_support_messages(self) -> list[SupportMessageEntity]:
        '''
        Retrieves all support messages from the PostgreSQL database, including user emails.
        Returns:
            list[SupportMessageEntity]: A list of all retrieved support messages with user emails.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the support messages from the PostgreSQL database.
        '''
        
        query = """
            SELECT s.id, s.user_id, u.email, s.description, s.status, s.subject, s.created_at
            FROM Support s
            LEFT JOIN Users u ON s.user_id = u.id;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                return [
                    SupportMessageEntity(
                        id=row[0],
                        user_id=row[1],
                        user_email=row[2],
                        description=row[3],
                        status=row[4],
                        subject=row[5],
                        created_at=row[6]
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
            

    def mark_done_support_messages(self, support_message_model: SupportMessageEntity)-> int:
        '''
        Marks a support message as done in the PostgreSQL database.
        Args:
            support_message_model (SupportMessageEntity): The support message entity to mark as done.
        Returns:
            int: The ID of the marked support message.
        Raises:
            psycopg2.Error: If an error occurs while marking the support message as done in the PostgreSQL database.
        '''
        
        query = """
            UPDATE Support
            SET status = %s::boolean
            WHERE id = %s
            RETURNING id;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (support_message_model.get_status(), support_message_model.get_id()))
                conn.commit()
                return cursor.fetchone()[0]

        