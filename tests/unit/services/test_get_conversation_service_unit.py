import pytest
from unittest.mock import MagicMock
from services.get_conversation_service import GetConversationService
from ports.get_conversation_port import GetConversationPort
from models.conversation_model import ConversationModel

@pytest.fixture
def get_conversation_port_mock():
    return MagicMock(spec=GetConversationPort)

@pytest.fixture
def get_conversation_service(get_conversation_port_mock):
    return GetConversationService(get_conversation_port_mock)

# Test get_conversation

def test_get_conversation_valid(get_conversation_service, get_conversation_port_mock):
    conversation = ConversationModel(id=1)
    get_conversation_port_mock.get_conversation.return_value = conversation

    result = get_conversation_service.get_conversation(conversation)
    
    assert result == conversation
    get_conversation_port_mock.get_conversation.assert_called_once_with(conversation)

def test_get_conversation_not_found(get_conversation_service, get_conversation_port_mock):
    conversation = ConversationModel(id=-1)
    get_conversation_port_mock.get_conversation.return_value = None

    result = get_conversation_service.get_conversation(conversation)
    
    assert result is None
    get_conversation_port_mock.get_conversation.assert_called_once_with(conversation)

def test_get_conversation_exception(get_conversation_service, get_conversation_port_mock):
    conversation = ConversationModel(id=2)
    get_conversation_port_mock.get_conversation.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        get_conversation_service.get_conversation(conversation)
    
    assert str(exc_info.value) == "Database error"
    get_conversation_port_mock.get_conversation.assert_called_once_with(conversation)
