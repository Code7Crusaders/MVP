import pytest
from unittest.mock import MagicMock
from services.save_support_message_service import SaveSupportMessageService
from models.support_message_model import SupportMessageModel
from ports.save_support_message_port import SaveSupportMessagePort

@pytest.fixture
def save_support_message_port_mock():
    return MagicMock(spec=SaveSupportMessagePort)

@pytest.fixture
def save_support_message_service(save_support_message_port_mock):
    return SaveSupportMessageService(save_support_message_port_mock)

# Test save_support_message

def test_save_support_message_valid(save_support_message_service, save_support_message_port_mock):
    support_message = SupportMessageModel(id="1")
    saved_message_id = 123  # Mock the saved support message's ID
    
    # Mock the port method to return the ID of the saved support message
    save_support_message_port_mock.save_support_message.return_value = saved_message_id
    
    result = save_support_message_service.save_support_message(support_message)
    
    assert result == saved_message_id
    save_support_message_port_mock.save_support_message.assert_called_once_with(support_message)

def test_save_support_message_exception(save_support_message_service, save_support_message_port_mock):
    support_message = SupportMessageModel(id="1")
    
    # Mock the port method to raise an exception
    save_support_message_port_mock.save_support_message.side_effect = Exception("Error saving support message")
    
    with pytest.raises(Exception) as exc_info:
        save_support_message_service.save_support_message(support_message)
    
    assert "Error saving support message" in str(exc_info.value)
    save_support_message_port_mock.save_support_message.assert_called_once_with(support_message)
