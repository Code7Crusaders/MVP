import pytest
from unittest.mock import MagicMock
from adapters.user_postgres_adapter import UserPostgresAdapter
from repositories.user_postgres_repository import UserPostgresRepository
from models.user_model import UserModel
from entities.user_entity import UserEntity

def test_register_success():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    
    user_model = MagicMock(spec=UserModel)
    user_model.get_username.return_value = "testuser"
    user_model.get_password.return_value = "securepass"
    user_model.get_email.return_value = "test@example.com"
    user_model.get_phone.return_value = "1234567890"
    user_model.get_first_name.return_value = "Test"
    user_model.get_last_name.return_value = "User"
    user_model.get_is_admin.return_value = False
    
    repo_mock.register.return_value = True
    
    result = adapter.register(user_model)
    assert result is True
    repo_mock.register.assert_called_once()

def test_register_failure():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    user_model = MagicMock(spec=UserModel)
    repo_mock.register.return_value = False
    
    result = adapter.register(user_model)
    assert result is False

def test_get_user_by_email():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    repo_mock.get_user_by_email.return_value = True
    
    result = adapter.get_user_by_email("test@example.com")
    assert result is True
    repo_mock.get_user_by_email.assert_called_once_with("test@example.com")

def test_get_user_by_username():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    repo_mock.get_user_by_username.return_value = True
    
    result = adapter.get_user_by_username("testuser")
    assert result is True
    repo_mock.get_user_by_username.assert_called_once_with("testuser")

def test_get_user_for_authentication_success():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    
    user_model = MagicMock(spec=UserModel)
    user_model.get_username.return_value = "testuser"
    
    user_entity = MagicMock(spec=UserEntity)
    user_entity.get_id.return_value = 1
    user_entity.get_username.return_value = "testuser"
    user_entity.get_password.return_value = "securepass"
    user_entity.get_email.return_value = "test@example.com"
    user_entity.get_phone.return_value = "1234567890"
    user_entity.get_first_name.return_value = "Test"
    user_entity.get_last_name.return_value = "User"
    user_entity.get_is_admin.return_value = False
    
    repo_mock.get_user_for_authentication.return_value = user_entity
    
    result = adapter.get_user_for_authentication(user_model)
    assert result.get_username() == "testuser"
    assert result.get_email() == "test@example.com"
    repo_mock.get_user_for_authentication.assert_called_once()

def test_get_user_for_authentication_failure():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    user_model = MagicMock(spec=UserModel)
    
    repo_mock.get_user_for_authentication.return_value = None
    
    with pytest.raises(Exception):
        adapter.get_user_for_authentication(user_model)

def test_register_exception():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    user_model = MagicMock(spec=UserModel)
    
    repo_mock.register.side_effect = Exception("Database error")
    
    with pytest.raises(Exception, match="Database error"):
        adapter.register(user_model)

def test_get_user_by_email_exception():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    
    repo_mock.get_user_by_email.side_effect = Exception("Database error")
    
    with pytest.raises(Exception, match="Database error"):
        adapter.get_user_by_email("test@example.com")

def test_get_user_for_authentication_exception():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    user_model = MagicMock(spec=UserModel)
    
    repo_mock.get_user_for_authentication.side_effect = Exception("Database error")
    
    with pytest.raises(Exception, match="Database error"):
        adapter.get_user_for_authentication(user_model)

def test_get_user_for_authentication_none():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)
    user_model = MagicMock(spec=UserModel)
    
    repo_mock.get_user_for_authentication.return_value = None
    
    with pytest.raises(Exception):
        adapter.get_user_for_authentication(user_model)

def test_get_user_by_username_exception():
    repo_mock = MagicMock(spec=UserPostgresRepository)
    adapter = UserPostgresAdapter(repo_mock)

    repo_mock.get_user_by_username.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        adapter.get_user_by_username("testuser")
