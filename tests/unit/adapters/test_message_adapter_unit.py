import pytest
from unittest.mock import MagicMock, call, ANY
from adapters.message_postgres_adapter import MessagePostgresAdapter
from repositories.message_postgres_repository import MessagePostgresRepository
from entities.message_entity import MessageEntity
from models.message_model import MessageModel
from models.conversation_model import ConversationModel

@pytest.fixture
def message_postgres_repository_mock():
    return MagicMock(spec=MessagePostgresRepository)

@pytest.fixture
def message_adapter(message_postgres_repository_mock):
    return MessagePostgresAdapter(message_postgres_repository_mock)

# Test get_message

def test_get_message_valid(message_adapter, message_postgres_repository_mock):
    message = MessageModel(id=1, text="Hello")
    message_postgres_repository_mock.get_message.return_value = message

    result = message_adapter.get_message(message)
    
    assert result.id == message.id
    assert result.text == message.text
    message_postgres_repository_mock.get_message.assert_called_once()

def test_get_message_invalid_id(message_adapter, message_postgres_repository_mock):
    invalid_message = MessageModel(id=-1, text="Hello")
    message_postgres_repository_mock.get_message.side_effect = Exception("Invalid ID")  
    
    with pytest.raises(Exception) as exc_info:
        message_adapter.get_message(invalid_message)
    
    assert str(exc_info.value) == "Invalid ID"
    message_postgres_repository_mock.get_message.assert_called_once()

# Test get_messages_by_conversation

def test_get_messages_by_conversation_valid(message_adapter, message_postgres_repository_mock):
    conversation = MessageModel(conversation_id=1)
    messages = [MessageModel(id=1, text="Hello"), MessageModel(id=2, text="Hi")]
    message_postgres_repository_mock.get_messages_by_conversation.return_value = messages

    result = message_adapter.get_messages_by_conversation(conversation)
    
    assert isinstance(result, list)
    assert len(result) == len(messages)
    for r, m in zip(result, messages):
        assert r.id == m.id
        assert r.text == m.text
    
    message_postgres_repository_mock.get_messages_by_conversation.assert_called_once()

def test_get_messages_by_conversation_empty(message_adapter, message_postgres_repository_mock):
    conversation = MessageModel(conversation_id=1)
    message_postgres_repository_mock.get_messages_by_conversation.return_value = []  

    result = message_adapter.get_messages_by_conversation(conversation)
    
    assert isinstance(result, list)
    assert result == []
    message_postgres_repository_mock.get_messages_by_conversation.assert_called_once()

def test_get_messages_by_conversation_exception(message_adapter, message_postgres_repository_mock):
    conversation = MessageModel(conversation_id=-1)
    message_postgres_repository_mock.get_messages_by_conversation.side_effect = Exception("Conversation not found")
    
    with pytest.raises(Exception) as exc_info:
        message_adapter.get_messages_by_conversation(conversation)
    
    assert str(exc_info.value) == "Conversation not found"
    message_postgres_repository_mock.get_messages_by_conversation.assert_called_once()

# Test save_message

def test_save_message_valid(message_adapter, message_postgres_repository_mock):
    message = MessageModel(id=-1, text="Hello")
    message_postgres_repository_mock.save_message.return_value = 1

    result = message_adapter.save_message(message)
    
    assert isinstance(result, int)
    assert result == 1
    message_postgres_repository_mock.save_message.assert_called_once()

def test_save_message_invalid_text(message_adapter, message_postgres_repository_mock):
    invalid_message = MessageModel(id=None, text="")
    message_postgres_repository_mock.save_message.side_effect = Exception("Invalid message data")  

    with pytest.raises(Exception) as exc_info:
        message_adapter.save_message(invalid_message)
    
    assert str(exc_info.value) == "Invalid message data"
    message_postgres_repository_mock.save_message.assert_called_once()

# Test update_message_rating

def test_update_message_rating_success(message_adapter, message_postgres_repository_mock):
    message = MessageModel(id=1, text=None, created_at=None, is_bot=None, conversation_id=None, rating=5)
    
    # Mock repository response
    message_postgres_repository_mock.update_message_rating.return_value = True

    result = message_adapter.update_message_rating(message)
    
    message_postgres_repository_mock.update_message_rating.assert_called_once_with(ANY)
    assert result is True


def test_update_message_rating_failure(message_adapter, message_postgres_repository_mock):
    message = MessageModel(id=1, text=None, created_at=None, is_bot=None, conversation_id=None, rating=5)
    
    # Simulate repository exception
    message_postgres_repository_mock.update_message_rating.side_effect = Exception("Failed to update rating")
    
    with pytest.raises(Exception, match="Failed to update rating"):
        message_adapter.update_message_rating(message)

def test_fetch_messages_success(message_adapter, message_postgres_repository_mock):
    messages = [
        MessageEntity(id=1, text="Message 1", created_at="2025-04-02", is_bot=False, conversation_id=1, rating=5),
        MessageEntity(id=2, text="Message 2", created_at="2025-04-02", is_bot=True, conversation_id=1, rating=4),
    ]
    
    # Mock repository response
    message_postgres_repository_mock.fetch_messages.return_value = messages

    result = message_adapter.fetch_messages()
    
    assert len(result) == 2
    assert result[0].get_text() == "Message 1"
    assert result[1].get_text() == "Message 2"
    assert result[0].get_rating() == 5
    assert result[1].get_rating() == 4


def test_fetch_messages_failure(message_adapter, message_postgres_repository_mock):
    # Simulate repository exception
    message_postgres_repository_mock.fetch_messages.side_effect = Exception("Failed to fetch messages")
    
    with pytest.raises(Exception, match="Failed to fetch messages"):
        message_adapter.fetch_messages()

