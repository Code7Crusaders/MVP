import psycopg2
from entities.template_entity import TemplateEntity

class TemplatePostgresRepository:
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

    def get_template(self, template_id: int) -> TemplateEntity:
        '''
        Retrieves a template from the PostgreSQL database by its ID.
        Args:
            template_id (int): The ID of the template to retrieve.
        Returns:
            TemplateEntity: The retrieved template.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the template from the PostgreSQL database.
        '''
        
        query = "SELECT id, question, answer, author, last_modified FROM Templates WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (template_id,))
                result = cursor.fetchone()
                if result:
                    return TemplateEntity(id=result[0], question=result[1], answer=result[2], author=result[3], last_modified=result[4])
                else:
                    return None
        

    def get_template_list(self) -> list[TemplateEntity]:
        '''
        Retrieves all templates from the Templates table.
        Returns:
            list[TemplateEntity]: A list of TemplateEntity objects.
        '''
        
        query = "SELECT id, question, answer, author, last_modified FROM Templates;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                return [TemplateEntity(id=row[0], question=row[1], answer=row[2], author=row[3], last_modified=row[4]) for row in rows]
        
    
    def save_template(self, question: str, answer: int, author: str) -> int:
        '''
        Saves a new template to the PostgreSQL database.
        Args:
            question (str): The question of the template.
            answer (str): The answer of the template.
            author (str): The author of the template.
        Returns:
            int: The ID of the newly created template.
        Raises:
            psycopg2.Error: If an error occurs while saving the template in the PostgreSQL database.
            ValueError: If the author does not exist in the Users table or if the template already exists.
        '''
        
        # Ensure the author exists in the Users table
        check_author_query = "SELECT id FROM Users WHERE id = %s;"
        check_template_query = "SELECT id FROM Templates WHERE question = %s AND answer = %s AND author = %s;"
        insert_query = "INSERT INTO Templates (question, answer, author) VALUES (%s, %s, %s) RETURNING id;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(check_author_query, (author,))
                author_exists = cursor.fetchone()
                if not author_exists:
                    raise ValueError(f"Author '{author}' does not exist in the Users table.")
                    
                # Check if the template already exists
                cursor.execute(check_template_query, (question, answer, author))
                template_exists = cursor.fetchone()
                if template_exists:
                    raise ValueError("A template with the same question, answer, and author already exists.")
                    
                cursor.execute(insert_query, (question, answer, author))
                new_template_id = cursor.fetchone()[0]
                conn.commit()
                return new_template_id
        
    def delete_template(self, template_id: int) -> bool:
        '''
        Deletes a template from the PostgreSQL database based on its ID.
        Args:
            template_id (int): The ID of the template to delete.
        Returns:
            bool: True if the template was deleted, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while deleting the template from the PostgreSQL database.
        '''
        
        delete_query = "DELETE FROM Templates WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, (template_id,))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                return False
