import pytest
from unittest.mock import MagicMock
from services.registration_service import RegistrationService
from ports.registration_port import RegistrationPort
from services.validation_service import ValidationService
from models.user_model import UserModel
from flask_bcrypt import Bcrypt

@pytest.fixture
def registration_port_mock():
    return MagicMock(RegistrationPort)

@pytest.fixture
def validation_service_mock():
    return MagicMock(ValidationService)

@pytest.fixture
def bcrypt_mock():
    return MagicMock(Bcrypt)

@pytest.fixture
def registration_service(registration_port_mock, validation_service_mock, bcrypt_mock):
    return RegistrationService(
        registration_port=registration_port_mock,
        validation_service=validation_service_mock,
        bcrypt=bcrypt_mock
    )

def test_register_success(registration_service, registration_port_mock, validation_service_mock, bcrypt_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="testuser",
        password="plaintextpassword",
        email="test@example.com",
        phone="123456789",
        first_name="Test",
        last_name="User",
        is_admin=False
    )

    # Mock dependencies
    bcrypt_mock.generate_password_hash.return_value = b"hashedpassword"
    registration_port_mock.register.return_value = True

    # Call the register method
    success = registration_service.register(input_user)

    # Assertions
    assert success is True
    validation_service_mock.validate_registration.assert_called_once_with(input_user)
    bcrypt_mock.generate_password_hash.assert_called_once_with("plaintextpassword")
    registration_port_mock.register.assert_called_once_with(input_user)

def test_register_validation_error(registration_service, validation_service_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="invaliduser",
        password="plaintextpassword",
        email="invalid@example.com",
        phone="123456789",
        first_name="Invalid",
        last_name="User",
        is_admin=False
    )

    # Mock validation to raise an exception
    validation_service_mock.validate_registration.side_effect = ValueError("Invalid registration data")

    # Call the register method and expect an exception
    with pytest.raises(ValueError, match="Invalid registration data"):
        registration_service.register(input_user)

    validation_service_mock.validate_registration.assert_called_once_with(input_user)

def test_register_database_error(registration_service, registration_port_mock, bcrypt_mock):
    # Mock input UserModel
    input_user = UserModel(
        username="testuser",
        password="plaintextpassword",
        email="test@example.com",
        phone="123456789",
        first_name="Test",
        last_name="User",
        is_admin=False
    )

    # Mock bcrypt and database errors
    bcrypt_mock.generate_password_hash.return_value = b"hashedpassword"
    registration_port_mock.register.side_effect = Exception("Database error")

    # Call the register method and expect an exception
    with pytest.raises(Exception, match="Database error"):
        registration_service.register(input_user)

    bcrypt_mock.generate_password_hash.assert_called_once_with("plaintextpassword")
    registration_port_mock.register.assert_called_once_with(input_user)
