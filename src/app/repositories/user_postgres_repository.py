import psycopg2
from models.user_model import UserModel


class PostgresRepository:
    def __init__(self, conn: psycopg2.extensions.connection):
        '''
        Initializes the PostgresRepository with the given database connection.
        Args:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
        '''
        self.__conn = conn

    def login(self, username: str, password: str) -> UserModel:
        # Implementation here
        pass

    def register(self, user: UserModel):
        # Implementation here
        pass
