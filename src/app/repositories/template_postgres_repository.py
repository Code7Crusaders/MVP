import psycopg2
from app.models.template_model import TemplateModel

class PostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        '''
        Initializes the PostgresRepository with the given database connection.
        Args:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
        '''
        self.__conn = conn

    def get_template_list(self) -> list[TemplateModel]:
        # Implementation here
        pass

    def get_random_template(self) -> TemplateModel:
        # Implementation here
        pass

    def save_template(self, template: TemplateModel):
        # Implementation here
        pass