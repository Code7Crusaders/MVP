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
        ConversationModel(id=1, title="Conversation 1", user_id=1),
        ConversationModel(id=2, title="Conversation 2", user_id=1)
    ]
    get_conversations_use_case_mock.get_conversations.return_value = conversations

    conversation_dto = ConversationDTO(id=None, title=None, user_id=1)
    result = get_conversations_controller.get_conversations(conversation_dto)
    
    assert len(result) == 2
    assert result[0].get_id() == 1
    assert result[0].get_title() == "Conversation 1"
    assert result[0].get_user_id() == 1
    assert result[1].get_id() == 2
    assert result[1].get_title() == "Conversation 2"
    assert result[1].get_user_id() == 1
    get_conversations_use_case_mock.get_conversations.assert_called_once()

def test_get_conversations_empty(get_conversations_controller, get_conversations_use_case_mock):
    get_conversations_use_case_mock.get_conversations.return_value = []
    
    conversation_dto = ConversationDTO(id=None, title=None, user_id=1)
    result = get_conversations_controller.get_conversations(conversation_dto)
    
    assert result == []
    get_conversations_use_case_mock.get_conversations.assert_called_once()

def test_get_conversations_exception(get_conversations_controller, get_conversations_use_case_mock):
    get_conversations_use_case_mock.get_conversations.side_effect = Exception("Database error")
    
    conversation_dto = ConversationDTO(id=None, title=None, user_id=1)
    
    with pytest.raises(Exception) as exc_info:
        get_conversations_controller.get_conversations(conversation_dto)
    
    assert str(exc_info.value) == "Database error"
    get_conversations_use_case_mock.get_conversations.assert_called_once()
