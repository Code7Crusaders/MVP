import pytest
from unittest.mock import MagicMock
from services.get_message_service import GetMessageService
from models.message_model import MessageModel
from ports.get_message_port import GetMessagePort

@pytest.fixture
def get_message_port_mock():
    return MagicMock(spec=GetMessagePort)

@pytest.fixture
def get_message_service(get_message_port_mock):
    return GetMessageService(get_message_port_mock)

# Test get_message

def test_get_message_valid(get_message_service, get_message_port_mock):
    message_id = "123"
    message = MessageModel(id=message_id)
    
    # Mock the port method to return the message
    get_message_port_mock.get_message.return_value = message
    
    result = get_message_service.get_message(message)
    
    assert result == message
    get_message_port_mock.get_message.assert_called_once_with(message)

def test_get_message_no_message(get_message_service, get_message_port_mock):
    message_id = "123"
    message = MessageModel(id=message_id)
    
    # Mock the port method to return None (or handle as appropriate)
    get_message_port_mock.get_message.return_value = None
    
    result = get_message_service.get_message(message)
    
    assert result is None
    get_message_port_mock.get_message.assert_called_once_with(message)

def test_get_message_exception(get_message_service, get_message_port_mock):
    message_id = "123"
    message = MessageModel(id=message_id)
    
    # Mock the port method to raise an exception
    get_message_port_mock.get_message.side_effect = Exception("Error retrieving message")
    
    with pytest.raises(Exception) as exc_info:
        get_message_service.get_message(message)
    
    assert "Error retrieving message" in str(exc_info.value)
    get_message_port_mock.get_message.assert_called_once_with(message)
