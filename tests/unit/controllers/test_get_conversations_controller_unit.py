import pytest
from unittest.mock import MagicMock
from controllers.get_conversations_controller import GetConversationsController
from usecases.get_conversations_useCase import GetConversationsUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

@pytest.fixture
def get_conversations_use_case_mock():
    return MagicMock(spec=GetConversationsUseCase)

@pytest.fixture
def get_conversations_controller(get_conversations_use_case_mock):
    return GetConversationsController(get_conversations_use_case_mock)

# Test get_conversations

def test_get_conversations_valid(get_conversations_controller, get_conversations_use_case_mock):
    conversations = [
        ConversationModel(id=1, title="Conversation 1"),
        ConversationModel(id=2, title="Conversation 2")
    ]
    get_conversations_use_case_mock.get_conversations.return_value = conversations

    result = get_conversations_controller.get_conversations()
    
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].title == "Conversation 1"
    assert result[1].id == 2
    assert result[1].title == "Conversation 2"
    get_conversations_use_case_mock.get_conversations.assert_called_once()

def test_get_conversations_empty(get_conversations_controller, get_conversations_use_case_mock):
    get_conversations_use_case_mock.get_conversations.return_value = []
    
    result = get_conversations_controller.get_conversations()
    
    assert result == []
    get_conversations_use_case_mock.get_conversations.assert_called_once()

def test_get_conversations_exception(get_conversations_controller, get_conversations_use_case_mock):
    get_conversations_use_case_mock.get_conversations.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        get_conversations_controller.get_conversations()
    
    assert str(exc_info.value) == "Database error"
    get_conversations_use_case_mock.get_conversations.assert_called_once()