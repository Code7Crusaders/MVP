import pytest
from unittest.mock import MagicMock
from services.save_message_service import SaveMessageService
from models.message_model import MessageModel
from ports.save_message_port import SaveMessagePort

@pytest.fixture
def save_message_port_mock():
    return MagicMock(spec=SaveMessagePort)

@pytest.fixture
def save_message_service(save_message_port_mock):
    return SaveMessageService(save_message_port_mock)

# Test save_message

def test_save_message_valid(save_message_service, save_message_port_mock):
    message = MessageModel(id="123")  # Created without content
    saved_message_id = 123  # Mock the saved message's ID
    
    # Mock the port method to return the ID of the saved message
    save_message_port_mock.save_message.return_value = saved_message_id
    
    result = save_message_service.save_message(message)
    
    assert result == saved_message_id
    save_message_port_mock.save_message.assert_called_once_with(message)

def test_save_message_exception(save_message_service, save_message_port_mock):
    message = MessageModel(id="123")  # Created without content
    
    # Mock the port method to raise an exception
    save_message_port_mock.save_message.side_effect = Exception("Error saving message")
    
    with pytest.raises(Exception) as exc_info:
        save_message_service.save_message(message)
    
    assert "Error saving message" in str(exc_info.value)
    save_message_port_mock.save_message.assert_called_once_with(message)
