from abc import ABC, abstractmethod
from models.user_model import UserModel

class RegistrationPort(ABC):

    @abstractmethod
    def register(self, user_model: UserModel)-> bool:
        """
        Register a new user.
        
        Args:
            user_model (UserModel): The user data transfer object.
        
        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """