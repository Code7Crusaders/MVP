from usecases.authentication_useCase import AuthenticationUseCase
from ports.authentication_port import AuthenticationPort
from models.user_model import UserModel

from flask_bcrypt import Bcrypt

class AuthenticationService(AuthenticationUseCase):
    
    def __init__(self, authentication_port: AuthenticationPort, bcrypt: Bcrypt ):
        self.authentication_port = authentication_port
        self.bcrypt = bcrypt
        

    def login(self, user_model: UserModel) -> UserModel:
        """
        Log in a user.

        Args:
            user_model (UserModel): The user model to log in.

        Returns:
            UserModel: The user model that was logged in.
        """        
        try:

            retrived_user = self.authentication_port.get_user_for_authentication(user_model)
            
            if retrived_user is None:
                raise ValueError("Credentials are not valid")
            if not self.bcrypt.check_password_hash(retrived_user.get_password(), user_model.get_password()):
                raise ValueError("Credentials are not valid")

            return retrived_user

        except Exception:
            raise ValueError("Credentials are not valid")
        





    