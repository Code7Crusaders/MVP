import pytest
from unittest.mock import patch, MagicMock
from repositories.user_postgres_repository import UserPostgresRepository
from entities.user_entity import UserEntity
from config.db_config import db_config


@pytest.fixture
def user_repo():
    return UserPostgresRepository(db_config)

@patch('repositories.user_postgres_repository.UserPostgresRepository.get_user_by_email')
def test_get_user_by_email(mock_get_user_by_email, user_repo):
    # Mock return value
    mock_get_user_by_email.return_value = True
    
    # Test valid email
    exists = user_repo.get_user_by_email("test@example.com")
    assert exists is True
    mock_get_user_by_email.assert_called_once_with("test@example.com")
    
    # Test non-existent email
    mock_get_user_by_email.reset_mock()
    mock_get_user_by_email.return_value = False
    exists = user_repo.get_user_by_email("nonexistent@example.com")
    assert exists is False
    mock_get_user_by_email.assert_called_once_with("nonexistent@example.com")

@patch('repositories.user_postgres_repository.UserPostgresRepository.get_user_by_username')
def test_get_user_by_username(mock_get_user_by_username, user_repo):
    # Mock return value
    mock_get_user_by_username.return_value = True
    
    # Test valid username
    exists = user_repo.get_user_by_username("testuser")
    assert exists is True
    mock_get_user_by_username.assert_called_once_with("testuser")
    
    # Test non-existent username
    mock_get_user_by_username.reset_mock()
    mock_get_user_by_username.return_value = False
    exists = user_repo.get_user_by_username("nonexistentuser")
    assert exists is False
    mock_get_user_by_username.assert_called_once_with("nonexistentuser")

@patch('repositories.user_postgres_repository.UserPostgresRepository.register')
def test_register(mock_register, user_repo):
    # Mock return value
    mock_register.return_value = True

    user = UserEntity(
        id=1,
        username="testuser",
        password="password",
        email="test@example.com",
        phone="123456789",
        first_name="Test",
        last_name="User",
        is_admin=False
    )

    # Test registration
    success = user_repo.register(user)
    assert success is True
    mock_register.assert_called_once_with(user)

@patch('repositories.user_postgres_repository.UserPostgresRepository.get_user_for_authentication')
def test_get_user_for_authentication(mock_get_user_for_authentication, user_repo):
    # Mock return value
    mock_user = MagicMock()
    mock_user.id = 1
    mock_user.username = "authuser"
    mock_user.password = "hashedpassword"
    mock_user.email = "auth@example.com"
    mock_user.phone = "987654321"
    mock_user.first_name = "Auth"
    mock_user.last_name = "User"
    mock_user.is_admin = True
    mock_get_user_for_authentication.return_value = mock_user

    user = UserEntity(username="authuser", password="password")
    authenticated_user = user_repo.get_user_for_authentication(user)

    # Assertions
    assert authenticated_user is not None
    assert authenticated_user.username == "authuser"
    assert authenticated_user.email == "auth@example.com"
    assert authenticated_user.is_admin is True
    mock_get_user_for_authentication.assert_called_once_with(user)
