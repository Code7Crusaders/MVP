import pytest
from unittest.mock import MagicMock
from controllers.registration_controller import RegistrationController
from usecases.registration_useCase import RegistrationUseCase
from dto.user_dto import UserDTO
from models.user_model import UserModel

@pytest.fixture
def registration_use_case_mock():
    return MagicMock(RegistrationUseCase)

@pytest.fixture
def registration_controller(registration_use_case_mock):
    return RegistrationController(registration_use_case=registration_use_case_mock)

def test_register_success(registration_controller, registration_use_case_mock):
    # Mock input DTO
    input_dto = UserDTO(
        username="newuser",
        password="newpassword",
        email="new@example.com",
        phone="123456789",
        first_name="New",
        last_name="User",
        is_admin=False
    )

    # Mock successful registration
    registration_use_case_mock.register.return_value = True

    # Call the register method
    success = registration_controller.register(input_dto)

    # Assertions
    assert success is True
    registration_use_case_mock.register.assert_called_once()
    
    # Verify that the UserModel created inside the controller is correct
    called_user_model = registration_use_case_mock.register.call_args[0][0]
    assert isinstance(called_user_model, UserModel)
    assert called_user_model.username == "newuser"
    assert called_user_model.password == "newpassword"
    assert called_user_model.email == "new@example.com"
    assert called_user_model.phone == "123456789"
    assert called_user_model.first_name == "New"
    assert called_user_model.last_name == "User"
    assert called_user_model.is_admin is False

def test_register_failure(registration_controller, registration_use_case_mock):
    # Mock input DTO
    input_dto = UserDTO(
        username="invaliduser",
        password="invalidpassword",
        email="invalid@example.com",
        phone="987654321",
        first_name="Invalid",
        last_name="User",
        is_admin=False
    )

    # Mock registration failure
    registration_use_case_mock.register.side_effect = Exception("Registration failed")

    # Call the register method and expect an exception
    with pytest.raises(Exception, match="Registration failed"):
        registration_controller.register(input_dto)

    registration_use_case_mock.register.assert_called_once()
    
    # Verify that the UserModel created inside the controller is correct
    called_user_model = registration_use_case_mock.register.call_args[0][0]
    assert isinstance(called_user_model, UserModel)
    assert called_user_model.username == "invaliduser"
    assert called_user_model.password == "invalidpassword"
    assert called_user_model.email == "invalid@example.com"
    assert called_user_model.phone == "987654321"
    assert called_user_model.first_name == "Invalid"
    assert called_user_model.last_name == "User"
    assert called_user_model.is_admin is False
