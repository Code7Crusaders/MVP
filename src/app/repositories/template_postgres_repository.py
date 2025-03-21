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

    def get_template(self, template: TemplateEntity) -> TemplateEntity:
        '''
        Retrieves a template from the PostgreSQL database using the provided template entity.
        Args:
            template (TemplateEntity): The template entity containing the ID of the template to retrieve.
        Returns:
            TemplateEntity: The retrieved template, or None if no template is found.
        Raises:
            psycopg2.Error: If an error occurs while retrieving the template from the PostgreSQL database.
        '''
        
        query = "SELECT id, question, answer, author, last_modified FROM Templates WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (template.get_id(),))
                result = cursor.fetchone()
                if result:
                    return TemplateEntity(id=result[0], question=result[1], answer=result[2], author_id=result[3], last_modified=result[4])
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
                return [TemplateEntity(id=row[0], question=row[1], answer=row[2], author_id=row[3], last_modified=row[4]) for row in rows]
        
    def save_template(self, template: TemplateEntity) -> int:
        '''
        Saves a new template to the PostgreSQL database.
        Args:
            template (TemplateEntity): The template entity to save.
        Returns:
            int: The ID of the newly created template.
        Raises:
            psycopg2.Error: If an error occurs while saving the template in the PostgreSQL database.
        '''
        query = """
            INSERT INTO Templates (question, answer, author, last_modified)
            VALUES (%s, %s, %s, %s)
        RETURNING id;
        """
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, (
                    template.get_question(), 
                    template.get_answer(), 
                    template.get_author_id(), 
                    template.get_last_modified()
                ))
                conn.commit()
                return cursor.fetchone()[0]
            
    def delete_template(self, template: TemplateEntity) -> bool:
        '''
        Deletes a template from the PostgreSQL database based on its ID.
        Args:
            template (TemplateEntity): The template entity containing the ID of the template to delete.
        Returns:
            bool: True if the template was deleted, False otherwise.
        Raises:
            psycopg2.Error: If an error occurs while deleting the template from the PostgreSQL database.
        '''
        
        delete_query = "DELETE FROM Templates WHERE id = %s;"
        with self.__connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, (template.get_id(),))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            else:
                return False