from abc import ABC, abstractmethod
from models.user_model import UserModel

class AuthenticationPort(ABC):

    @abstractmethod
    def get_user_for_authentication(self, user_model: UserModel) -> UserModel:
        """
        Authenticate and retrieve a user.

        Args:
            user_model (UserModel): The user model to authenticate.

        Returns:
            UserModel: The authenticated user model.
        """