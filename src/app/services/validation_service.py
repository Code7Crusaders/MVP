from ports.validation_port import ValidationPort
from models.user_model import UserModel

class ValidationService:
    """
    The ValidationService class is responsible for validating user data.
    """
    
    def __init__(self, validation_port: ValidationPort):
        self.validation_port = validation_port

    def validate_registration(self, user_model: UserModel) -> None:
        """
        Validates the user registration based on database constraints.
        
        Args:
            user_model (UserModel): The user model to validate.
        
        Raises:
            ValueError: If email or username already exists.
        """
        # Check if email already exists 
        if self.validation_port.get_user_by_email(user_model.get_email()):
            raise ValueError("Email is already in use.")

        # Check if username already exists 
        if self.validation_port.get_user_by_username(user_model.get_username()):
            raise ValueError("Username is already taken.")
