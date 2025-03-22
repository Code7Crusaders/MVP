import pytest
from unittest.mock import MagicMock
from services.save_conversation_title_service import SaveConversationTitleService
from models.conversation_model import ConversationModel
from ports.save_conversation_title_port import SaveConversationTitlePort

@pytest.fixture
def save_conversation_title_port_mock():
    return MagicMock(spec=SaveConversationTitlePort)

@pytest.fixture
def save_conversation_title_service(save_conversation_title_port_mock):
    return SaveConversationTitleService(save_conversation_title_port_mock)

# Test save_conversation_title

def test_save_conversation_title_valid(save_conversation_title_service, save_conversation_title_port_mock):
    conversation = ConversationModel(id="1", title="New Conversation Title")
    updated_conversation_id = 123  # Mock the updated conversation's ID
    
    # Mock the port method to return the ID of the saved conversation
    save_conversation_title_port_mock.save_conversation_title.return_value = updated_conversation_id
    
    result = save_conversation_title_service.save_conversation_title(conversation)
    
    assert result == updated_conversation_id
    save_conversation_title_port_mock.save_conversation_title.assert_called_once_with(conversation)

def test_save_conversation_title_exception(save_conversation_title_service, save_conversation_title_port_mock):
    conversation = ConversationModel(id="1", title="New Conversation Title")
    
    # Mock the port method to raise an exception
    save_conversation_title_port_mock.save_conversation_title.side_effect = Exception("Error saving conversation title")
    
    with pytest.raises(Exception) as exc_info:
        save_conversation_title_service.save_conversation_title(conversation)
    
    assert "Error saving conversation title" in str(exc_info.value)
    save_conversation_title_port_mock.save_conversation_title.assert_called_once_with(conversation)
