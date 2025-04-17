
from usecases.registration_useCase import RegistrationUseCase
from ports.registration_port import RegistrationPort
from services.validation_service import ValidationService
from models.user_model import UserModel

from flask_bcrypt import Bcrypt

class RegistrationService(RegistrationUseCase):
        
    def __init__(self, registration_port: RegistrationPort, validation_service: ValidationService, bcrypt: Bcrypt):
        self.bcrypt = bcrypt
        self.validation_service = validation_service
        self.registration_port = registration_port

    def register(self, user_model : UserModel) -> bool:
        """
        Register a new user.
        
        Args:
            user_dto (UserModel): The user data transfer object.
        
        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """
        try:
            self.validation_service.validate_registration(user_model)

            user_model.set_password(self.bcrypt.generate_password_hash(user_model.get_password()).decode('utf-8'))

            return self.registration_port.register(user_model)
        
        except Exception as e:
            raise e
