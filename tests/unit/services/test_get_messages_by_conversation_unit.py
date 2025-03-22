import pytest
from unittest.mock import MagicMock
from services.get_messages_by_conversation_service import GetMessagesByConversationService
from models.message_model import MessageModel
from ports.get_messages_by_conversation_port import GetMessagesByConversationPort

@pytest.fixture
def get_messages_by_conversation_port_mock():
    return MagicMock(spec=GetMessagesByConversationPort)

@pytest.fixture
def get_messages_by_conversation_service(get_messages_by_conversation_port_mock):
    return GetMessagesByConversationService(get_messages_by_conversation_port_mock)

# Test get_messages_by_conversation

def test_get_messages_by_conversation_valid(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)
    messages = [MessageModel(id="msg_1"), MessageModel(id="msg_2")]
    
    # Mock the port method to return a list of messages
    get_messages_by_conversation_port_mock.get_messages_by_conversation.return_value = messages
    
    result = get_messages_by_conversation_service.get_messages_by_conversation(conversation)
    
    assert result == messages
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)

def test_get_messages_by_conversation_no_messages(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)
    messages = []
    
    # Mock the port method to return an empty list
    get_messages_by_conversation_port_mock.get_messages_by_conversation.return_value = messages
    
    result = get_messages_by_conversation_service.get_messages_by_conversation(conversation)
    
    assert result == messages
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)

def test_get_messages_by_conversation_exception(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)
    
    # Mock the port method to raise an exception
    get_messages_by_conversation_port_mock.get_messages_by_conversation.side_effect = Exception("Error retrieving messages")
    
    with pytest.raises(Exception) as exc_info:
        get_messages_by_conversation_service.get_messages_by_conversation(conversation)
    
    assert "Error retrieving messages" in str(exc_info.value)
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)
