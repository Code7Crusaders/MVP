import pytest
from unittest.mock import MagicMock
from services.validation_service import ValidationService
from ports.validation_port import ValidationPort
from models.user_model import UserModel

@pytest.fixture
def validation_port_mock():
    return MagicMock(ValidationPort)

@pytest.fixture
def validation_service(validation_port_mock):
    return ValidationService(validation_port=validation_port_mock)

def test_validate_registration_success(validation_service, validation_port_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="newuser",
        password="newpassword",
        email="newuser@example.com",
        phone="123456789",
        first_name="New",
        last_name="User",
        is_admin=False
    )

    # Simula che il nome utente e l'email non esistono nel database
    validation_port_mock.get_user_by_username.return_value = False
    validation_port_mock.get_user_by_email.return_value = False

    # Call the validate_registration method
    validation_service.validate_registration(input_user)

    # Assertions
    validation_port_mock.get_user_by_username.assert_called_once_with("newuser")
    validation_port_mock.get_user_by_email.assert_called_once_with("newuser@example.com")

def test_validate_registration_username_taken(validation_service, validation_port_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="takenuser",
        password="password",
        email="user@example.com",
        phone="123456789",
        first_name="Taken",
        last_name="User",
        is_admin=False
    )

    # Simula che il nome utente esiste nel database
    validation_port_mock.get_user_by_username.return_value = True

    # Call the validate_registration method and expect an exception
    with pytest.raises(ValueError, match="Username is already taken."):
        validation_service.validate_registration(input_user)

    validation_port_mock.get_user_by_username.assert_called_once_with("takenuser")
    validation_port_mock.get_user_by_email.assert_not_called()

def test_validate_registration_email_taken(validation_service, validation_port_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="newuser",
        password="password",
        email="takenemail@example.com",
        phone="123456789",
        first_name="New",
        last_name="User",
        is_admin=False
    )

    # Simula che l'email esiste nel database
    validation_port_mock.get_user_by_username.return_value = False
    validation_port_mock.get_user_by_email.return_value = True

    # Call the validate_registration method and expect an exception
    with pytest.raises(ValueError, match="Email is already in use."):
        validation_service.validate_registration(input_user)

    validation_port_mock.get_user_by_username.assert_called_once_with("newuser")
    validation_port_mock.get_user_by_email.assert_called_once_with("takenemail@example.com")
