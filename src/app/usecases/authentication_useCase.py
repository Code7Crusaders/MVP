from abc import ABC, abstractmethod
from models.user_model import UserModel

class AuthenticationUseCase(ABC):

    def login(self, user_model: UserModel) -> UserModel:
        """
        Log in a user.

        Args:
            user_model (UserModel): The user model to log in.

        Returns:
            UserModel: The user model that was logged in.
        """