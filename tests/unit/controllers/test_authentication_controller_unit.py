import pytest
from unittest.mock import MagicMock, patch
from controllers.authentication_controller import AuthenticationController
from usecases.authentication_useCase import AuthenticationUseCase
from dto.user_dto import UserDTO
from models.user_model import UserModel

@pytest.fixture
def authentication_use_case_mock():
    return MagicMock(AuthenticationUseCase)

@pytest.fixture
def authentication_controller(authentication_use_case_mock):
    return AuthenticationController(authentication_use_case=authentication_use_case_mock)

def test_login_success(authentication_controller, authentication_use_case_mock):
    # Mock input DTO
    input_dto = UserDTO(
        username="testuser",
        password="testpassword"
    )

    # Mock output UserModel
    mock_user_model = MagicMock(UserModel)
    mock_user_model.get_id.return_value = 1
    mock_user_model.get_username.return_value = "testuser"
    mock_user_model.get_password.return_value = "hashedpassword"
    mock_user_model.get_email.return_value = "test@example.com"
    mock_user_model.get_phone.return_value = "123456789"
    mock_user_model.get_first_name.return_value = "Test"
    mock_user_model.get_last_name.return_value = "User"
    mock_user_model.get_is_admin.return_value = False

    authentication_use_case_mock.login.return_value = mock_user_model

    # Call the login method
    result_dto = authentication_controller.login(input_dto)

    # Assertions
    assert result_dto is not None
    assert result_dto.id == 1
    assert result_dto.username == "testuser"
    assert result_dto.password == "hashedpassword"
    assert result_dto.email == "test@example.com"
    assert result_dto.phone == "123456789"
    assert result_dto.first_name == "Test"
    assert result_dto.last_name == "User"
    assert result_dto.is_admin is False

    authentication_use_case_mock.login.assert_called_once()
    
    # Verifica che l'istanza di UserModel abbia i valori corretti
    called_user_model = authentication_use_case_mock.login.call_args[0][0]
    assert isinstance(called_user_model, UserModel)
    assert called_user_model.username == "testuser"
    assert called_user_model.password == "testpassword"

def test_login_failure(authentication_controller, authentication_use_case_mock):
    # Mock input DTO
    input_dto = UserDTO(
        username="wronguser",
        password="wrongpassword"
    )

    # Mock login failure
    authentication_use_case_mock.login.side_effect = Exception("Authentication failed")

    # Call the login method and expect an exception
    with pytest.raises(Exception, match="Authentication failed"):
        authentication_controller.login(input_dto)

    authentication_use_case_mock.login.assert_called_once()
    
    # Verifica che l'istanza di UserModel abbia i valori corretti
    called_user_model = authentication_use_case_mock.login.call_args[0][0]
    assert isinstance(called_user_model, UserModel)
    assert called_user_model.username == "wronguser"
    assert called_user_model.password == "wrongpassword"
