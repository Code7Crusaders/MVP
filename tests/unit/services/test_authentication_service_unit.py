import pytest
from unittest.mock import MagicMock, patch
from services.authentication_service import AuthenticationService
from ports.authentication_port import AuthenticationPort
from models.user_model import UserModel
from flask_bcrypt import Bcrypt

@pytest.fixture
def authentication_port_mock():
    return MagicMock(AuthenticationPort)

@pytest.fixture
def bcrypt_mock():
    return MagicMock(Bcrypt)

@pytest.fixture
def authentication_service(authentication_port_mock, bcrypt_mock):
    return AuthenticationService(authentication_port=authentication_port_mock, bcrypt=bcrypt_mock)

def test_login_success(authentication_service, authentication_port_mock, bcrypt_mock):
    # Mock input UserModel
    input_user = UserModel(username="testuser", password="plaintextpassword")

    # Mock retrieved user from the port
    mock_retrieved_user = MagicMock(UserModel)
    mock_retrieved_user.get_password.return_value = "hashedpassword"
    authentication_port_mock.get_user_for_authentication.return_value = mock_retrieved_user

    # Mock bcrypt check
    bcrypt_mock.check_password_hash.return_value = True

    # Call the login method
    logged_in_user = authentication_service.login(input_user)

    # Assertions
    assert logged_in_user is not None
    assert logged_in_user == mock_retrieved_user
    authentication_port_mock.get_user_for_authentication.assert_called_once_with(input_user)
    bcrypt_mock.check_password_hash.assert_called_once_with("hashedpassword", "plaintextpassword")

def test_login_invalid_user(authentication_service, authentication_port_mock, bcrypt_mock):
    # Mock input UserModel
    input_user = UserModel(username="invaliduser", password="invalidpassword")

    # Mock retrieved user as None
    authentication_port_mock.get_user_for_authentication.return_value = None

    # Call the login method and expect an exception
    with pytest.raises(ValueError, match="Credentials are not valid"):
        authentication_service.login(input_user)

    authentication_port_mock.get_user_for_authentication.assert_called_once_with(input_user)
    bcrypt_mock.check_password_hash.assert_not_called()

def test_login_invalid_password(authentication_service, authentication_port_mock, bcrypt_mock):
    # Mock input UserModel
    input_user = UserModel(username="testuser", password="wrongpassword")

    # Mock retrieved user from the port
    mock_retrieved_user = MagicMock(UserModel)
    mock_retrieved_user.get_password.return_value = "hashedpassword"
    authentication_port_mock.get_user_for_authentication.return_value = mock_retrieved_user

    # Mock bcrypt check to return False
    bcrypt_mock.check_password_hash.return_value = False

    # Call the login method and expect an exception
    with pytest.raises(ValueError, match="Credentials are not valid"):
        authentication_service.login(input_user)

    authentication_port_mock.get_user_for_authentication.assert_called_once_with(input_user)
    bcrypt_mock.check_password_hash.assert_called_once_with("hashedpassword", "wrongpassword")
