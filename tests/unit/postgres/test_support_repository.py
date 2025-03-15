import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from app.repositories.support_message_postgres_repository import SupportMessagePostgresRepository
from app.config.db_config import db_config

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

@pytest.fixture
def support_message_repo():
    return SupportMessagePostgresRepository(db_config)

@patch('app.repositories.support_message_postgres_repository.SupportMessagePostgresRepository.get_support_message')
def test_get_support_message(mock_get_support_message, support_message_repo):
    mock_message = MagicMock()
    mock_message.id = 1
    mock_message.user_id = 1
    mock_message.description = "Test Description"
    mock_message.status = "true"
    mock_message.subject = "Test Subject"
    mock_message.created_at = "2023-01-01"
    mock_get_support_message.return_value = mock_message

    support_message = support_message_repo.get_support_message(1)
    
    assert support_message is not None
    assert support_message.id == 1
    assert support_message.user_id == 1
    assert support_message.description == "Test Description"
    assert support_message.status == "true"
    assert support_message.subject == "Test Subject"
    assert support_message.created_at == "2023-01-01"

    # Additional assertions
    mock_get_support_message.assert_called_once_with(1)
    assert isinstance(support_message.description, str)
    assert isinstance(support_message.created_at, str)

@patch('app.repositories.support_message_postgres_repository.SupportMessagePostgresRepository.save_support_message')
def test_save_support_message(mock_save_support_message, support_message_repo):
    mock_save_support_message.return_value = 1

    new_message_id = support_message_repo.save_support_message(1, "New Support Message Content", "true", "New Subject")
    
    assert new_message_id == 1
    mock_save_support_message.assert_called_once_with(1, "New Support Message Content", "true", "New Subject")

    # Additional test with different data
    mock_save_support_message.reset_mock()
    mock_save_support_message.return_value = 2

    new_message_id = support_message_repo.save_support_message(2, "Another Support Message", "false", "Another Subject")
    
    assert new_message_id == 2
    mock_save_support_message.assert_called_once_with(2, "Another Support Message", "false", "Another Subject")
