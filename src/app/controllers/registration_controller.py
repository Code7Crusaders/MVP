from usecases.registration_useCase import RegistrationUseCase
from dto.user_dto import UserDTO 
from models.user_model import UserModel

class RegistrationController:

    def __init__(self, registration_use_case: RegistrationUseCase):
        self.registration_use_case = registration_use_case

    def register(self, user_dto : UserDTO) -> bool:
        """
        Register a new user.
        
        Args:
            user_dto (UserDTO): The user data transfer object.
        
        Returns:
            bool: True if the user was registered successfully, False otherwise.
        """
        try:

            user_model = UserModel(
                username=user_dto.get_username(),
                password=user_dto.get_password(),
                email=user_dto.get_email(),
                phone=user_dto.get_phone(),
                first_name=user_dto.get_first_name(),
                last_name=user_dto.get_last_name(),
                is_admin=user_dto.get_is_admin()
            )
            
            return self.registration_use_case.register(user_model)
        
        except Exception as e:
            raise e