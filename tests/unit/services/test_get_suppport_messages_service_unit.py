import pytest
from unittest.mock import MagicMock
from services.get_support_messages_service import GetSupportMessagesService
from models.support_message_model import SupportMessageModel
from ports.get_support_messages_port import GetSupportMessagesPort

@pytest.fixture
def get_support_messages_port_mock():
    return MagicMock(spec=GetSupportMessagesPort)

@pytest.fixture
def get_support_messages_service(get_support_messages_port_mock):
    return GetSupportMessagesService(get_support_messages_port_mock)

# Test get_support_messages

def test_get_support_messages_valid(get_support_messages_service, get_support_messages_port_mock):
    support_messages = [
        SupportMessageModel(id="1"),
        SupportMessageModel(id="2"),
    ]
    
    # Mock the port method to return a list of support messages
    get_support_messages_port_mock.get_support_messages.return_value = support_messages
    
    result = get_support_messages_service.get_support_messages()
    
    assert result == support_messages
    get_support_messages_port_mock.get_support_messages.assert_called_once()

def test_get_support_messages_no_messages(get_support_messages_service, get_support_messages_port_mock):
    support_messages = []  # Empty list for no messages
    
    # Mock the port method to return an empty list
    get_support_messages_port_mock.get_support_messages.return_value = support_messages
    
    result = get_support_messages_service.get_support_messages()
    
    assert result == support_messages
    get_support_messages_port_mock.get_support_messages.assert_called_once()

def test_get_support_messages_exception(get_support_messages_service, get_support_messages_port_mock):
    # Mock the port method to raise an exception
    get_support_messages_port_mock.get_support_messages.side_effect = Exception("Error retrieving support messages")
    
    with pytest.raises(Exception) as exc_info:
        get_support_messages_service.get_support_messages()
    
    assert "Error retrieving support messages" in str(exc_info.value)
    get_support_messages_port_mock.get_support_messages.assert_called_once()
