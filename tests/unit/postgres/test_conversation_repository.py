import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from config.db_config import db_config

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

@pytest.fixture
def conversation_repo():
    return ConversationPostgresRepository(db_config)

@patch('repositories.conversation_postgres_repository.ConversationPostgresRepository.get_conversation')
def test_get_conversation(mock_get_conversation, conversation_repo):
    # Test case where conversation is found
    mock_conversation = MagicMock()
    mock_conversation.id = 4
    mock_conversation.title = "Test Conversation"
    mock_get_conversation.return_value = mock_conversation

    conversation = conversation_repo.get_conversation(4)
    
    assert conversation is not None
    assert conversation.id == 4
    assert conversation.title == "Test Conversation"

    # Test case where conversation is not found
    mock_get_conversation.return_value = None

    conversation = conversation_repo.get_conversation(999)
    
    assert conversation is None

@patch('repositories.conversation_postgres_repository.ConversationPostgresRepository.save_conversation_title')
def test_save_conversation_title(mock_save_conversation_title, conversation_repo):
    # Test case where save is successful
    mock_save_conversation_title.return_value = None

    conversation_repo.save_conversation_title(4, "Oi")
    
    mock_save_conversation_title.assert_called_once_with(4, "Oi")

    # Test case where save fails
    mock_save_conversation_title.side_effect = Exception("Database error")

    with pytest.raises(Exception) as excinfo:
        conversation_repo.save_conversation_title(4, "Oi")
    
    assert str(excinfo.value) == "Database error"
    mock_save_conversation_title.assert_called_with(4, "Oi")
