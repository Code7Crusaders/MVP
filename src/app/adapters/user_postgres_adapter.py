from ports.registration_port import RegistrationPort
from ports.validation_port import ValidationPort

from repositories.user_postgres_repository import UserPostgresRepository

from models.user_model import UserModel

from entities.user_entity import UserEntity



class UserPostgresAdapter(RegistrationPort, ValidationPort):

    def __init__(self, user_postgres_repository: UserPostgresRepository):
        self.user_postgres_repository = user_postgres_repository
        
    
    def register(self, user_model: UserModel)-> bool:
        """
        Register a new user.
        
        Args:
            user_model (UserModel): The user data transfer object.
        
        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """

        try:
            user_entity = UserEntity(
                username=user_model.get_username(),
                password=user_model.get_password(),
                email=user_model.get_email(),
                phone=user_model.get_phone(),
                first_name=user_model.get_first_name(),
                last_name=user_model.get_last_name(),
                is_admin=user_model.get_is_admin()
            )

            return self.user_postgres_repository.register(user_entity)
        
        except Exception as e:
            raise e

        
    def get_user_by_email(self, email: str) -> bool:
        """
        Get a user by email.
        
        Args:
            email (str): The email of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """

        try:
            return self.user_postgres_repository.get_user_by_email(email)
        except Exception as e:
            raise e


    def get_user_by_username(self, username: str) -> bool:
        """
        Get a user by username.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            bool: True if the user exists, False otherwise.
        """
        
        try:
            return self.user_postgres_repository.get_user_by_username(username)
        except Exception as e:
            raise e
