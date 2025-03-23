import pytest
from unittest.mock import MagicMock
from controllers.get_conversation_controller import GetConversationController
from usecases.get_conversation_useCase import GetConversationUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

@pytest.fixture
def get_conversation_use_case_mock():
    return MagicMock(spec=GetConversationUseCase)

@pytest.fixture
def get_conversation_controller(get_conversation_use_case_mock):
    return GetConversationController(get_conversation_use_case_mock)

# Test get_conversation

def test_get_conversation_valid(get_conversation_controller, get_conversation_use_case_mock):
    conversation_dto = ConversationDTO(id=1, title="Test Conversation")
    conversation_model = ConversationModel(id=1, title="Test Conversation")
    get_conversation_use_case_mock.get_conversation.return_value = conversation_model

    result = get_conversation_controller.get_conversation(conversation_dto)
    
    assert result.id == 1
    assert result.title == "Test Conversation"
    get_conversation_use_case_mock.get_conversation.assert_called_once()


def test_get_conversation_exception(get_conversation_controller, get_conversation_use_case_mock):
    conversation_dto = ConversationDTO(id=2, title="Error Case")
    get_conversation_use_case_mock.get_conversation.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        get_conversation_controller.get_conversation(conversation_dto)
    
    assert str(exc_info.value) == "Database error"
    get_conversation_use_case_mock.get_conversation.assert_called_once()
