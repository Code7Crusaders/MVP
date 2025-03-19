
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from repositories.message_postgres_repository import MessagePostgresRepository
from config.db_config import db_config
from entities.message_entity import MessageEntity


@pytest.fixture
def message_repo():
    return MessagePostgresRepository(db_config)

@patch('repositories.message_postgres_repository.MessagePostgresRepository.get_message')
def test_get_message(mock_get_message, message_repo):
    # Test case where message is found
    mock_message = MagicMock()
    mock_message.id = 30
    mock_message.text = "Hello World"
    mock_get_message.return_value = mock_message

    message = message_repo.get_message(30)
    
    assert message is not None
    assert message.id == 30
    assert message.text == "Hello World"

    # Test case where message is not found
    mock_get_message.return_value = None

    message = message_repo.get_message(999)
    
    assert message is None

@patch('repositories.message_postgres_repository.MessagePostgresRepository.save_message')
def test_save_message(mock_save_message, message_repo):
    # Test case where save is successful
    mock_save_message.return_value = None

    message = MessageEntity(
        id=None,
        text="Hello World",
        created_at=datetime.now(),
        user_id=1,
        conversation_id=1,
        rating=False
    )
    message_repo.save_message(message)
    
    mock_save_message.assert_called_once_with(message)

    # Test case where save fails
    mock_save_message.side_effect = Exception("Database error")

    with pytest.raises(Exception) as excinfo:
        message_repo.save_message(message)
    
    assert str(excinfo.value) == "Database error"
    mock_save_message.assert_called_with(message)

@patch('repositories.message_postgres_repository.MessagePostgresRepository.get_messages_by_conversation')
def test_get_messages_by_conversation(mock_get_messages_by_conversation, message_repo):
    # Test case where messages are found
    mock_message1 = MagicMock()
    mock_message1.id = 1
    mock_message1.text = "Hello World"
    
    mock_message2 = MagicMock()
    mock_message2.id = 2
    mock_message2.text = "Hi again"
    
    mock_get_messages_by_conversation.return_value = [mock_message1, mock_message2]

    messages = message_repo.get_messages_by_conversation(1)
    
    assert len(messages) == 2
    assert messages[0].id == 1
    assert messages[0].text == "Hello World"
    assert messages[1].id == 2
    assert messages[1].text == "Hi again"

    # Test case where no messages are found
    mock_get_messages_by_conversation.return_value = []

    messages = message_repo.get_messages_by_conversation(999)
    
    assert len(messages) == 0