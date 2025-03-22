import pytest
from unittest.mock import MagicMock
from services.get_support_message_service import GetSupportMessageService
from models.support_message_model import SupportMessageModel
from ports.get_support_message_port import GetSupportMessagePort

@pytest.fixture
def get_support_message_port_mock():
    return MagicMock(spec=GetSupportMessagePort)

@pytest.fixture
def get_support_message_service(get_support_message_port_mock):
    return GetSupportMessageService(get_support_message_port_mock)

# Test get_support_message

def test_get_support_message_valid(get_support_message_service, get_support_message_port_mock):
    message_id = "123"
    message = SupportMessageModel(id=message_id)
    
    # Mock the port method to return the support message
    get_support_message_port_mock.get_support_message.return_value = message
    
    result = get_support_message_service.get_support_message(message)
    
    assert result == message
    get_support_message_port_mock.get_support_message.assert_called_once_with(message)

def test_get_support_message_no_message(get_support_message_service, get_support_message_port_mock):
    message_id = "123"
    message = SupportMessageModel(id=message_id)
    
    # Mock the port method to return None (if no message is found)
    get_support_message_port_mock.get_support_message.return_value = None
    
    result = get_support_message_service.get_support_message(message)
    
    assert result is None
    get_support_message_port_mock.get_support_message.assert_called_once_with(message)

def test_get_support_message_exception(get_support_message_service, get_support_message_port_mock):
    message_id = "123"
    message = SupportMessageModel(id=message_id)
    
    # Mock the port method to raise an exception
    get_support_message_port_mock.get_support_message.side_effect = Exception("Error retrieving support message")
    
    with pytest.raises(Exception) as exc_info:
        get_support_message_service.get_support_message(message)
    
    assert "Error retrieving support message" in str(exc_info.value)
    get_support_message_port_mock.get_support_message.assert_called_once_with(message)
