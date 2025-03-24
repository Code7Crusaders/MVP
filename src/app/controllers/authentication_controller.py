from usecases.authentication_useCase import AuthenticationUseCase
from dto.user_dto import UserDTO 
from models.user_model import UserModel

class AuthenticationController:

    def __init__(self, authentication_use_case: AuthenticationUseCase):
        self.authentication_use_case = authentication_use_case

    def login(self, user_dto : UserDTO) -> UserDTO:
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
                password=user_dto.get_password()
            )
            
            user_result = self.authentication_use_case.login(user_model)

            return UserDTO(
                id=user_result.get_id(),
                username=user_result.get_username(),
                password=user_result.get_password(),
                email=user_result.get_email(),
                phone=user_result.get_phone(),
                first_name=user_result.get_first_name(),
                last_name=user_result.get_last_name(),
                is_admin=user_result.get_is_admin()
            ) 
        
        except Exception as e:
            raise e