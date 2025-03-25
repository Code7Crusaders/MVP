import pytest
from unittest.mock import MagicMock
from services.get_conversations_service import GetConversationsService
from ports.get_conversations_port import GetConversationsPort
from models.conversation_model import ConversationModel

@pytest.fixture
def get_conversations_port_mock():
    return MagicMock(spec=GetConversationsPort)

@pytest.fixture
def get_conversations_service(get_conversations_port_mock):
    return GetConversationsService(get_conversations_port_mock)

# Test get_conversations

def test_get_conversations_valid(get_conversations_service, get_conversations_port_mock):
    conversations = [ConversationModel(id=1), ConversationModel(id=2)]
    get_conversations_port_mock.get_conversations.return_value = conversations

    # Suppose conversation are conversation of user_id = 1
    user_id = 1

    result = get_conversations_service.get_conversations(user_id)
    
    assert result == conversations
    get_conversations_port_mock.get_conversations.assert_called_once()

def test_get_conversations_empty(get_conversations_service, get_conversations_port_mock):
    get_conversations_port_mock.get_conversations.return_value = []

    # Suppose conversation are conversation of user_id = 1
    user_id = 1

    result = get_conversations_service.get_conversations(user_id)
    
    assert result == []
    get_conversations_port_mock.get_conversations.assert_called_once()

def test_get_conversations_exception(get_conversations_service, get_conversations_port_mock):
    get_conversations_port_mock.get_conversations.side_effect = Exception("Database error")

    # Suppose conversation are conversation of user_id = 1
    user_id = 1
    
    with pytest.raises(Exception) as exc_info:
        get_conversations_service.get_conversations(user_id)
    
    assert str(exc_info.value) == "Database error"
    get_conversations_port_mock.get_conversations.assert_called_once()
