import psycopg2

from entities.user_entity import UserEntity


class UserPostgresRepository:

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

    def register(self, user_model: UserEntity)-> bool:
        """
        Register a new user.
        
        Args:
            user_model (UserModel): The user data transfer object.
        
        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """

    def get_user_by_email(self, email: str) -> bool:
        """
        Get a user by email.
        
        Args:
            email (str): The email of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """

    def get_user_by_username(self, username: str) -> bool:
        """
        Get a user by username.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """
        