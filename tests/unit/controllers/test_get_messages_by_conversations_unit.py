import pytest
from unittest.mock import MagicMock
from controllers.get_messages_by_conversation_controller import GetMessagesByConversationController
from usecases.get_messages_by_conversation_useCase import GetMessagesByConversationUseCase
from dto.message_dto import MessageDTO

@pytest.fixture
def get_messages_by_conversation_use_case_mock():
    return MagicMock(spec=GetMessagesByConversationUseCase)

@pytest.fixture
def get_messages_by_conversation_controller(get_messages_by_conversation_use_case_mock):
    return GetMessagesByConversationController(get_messages_by_conversation_use_case_mock)

# Test get_messages_by_conversation

def test_get_messages_by_conversation_valid(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    conversation_dto = MessageDTO(id=None, text=None, is_bot=None, conversation_id="conv1", rating=None, created_at=None)

    messages_models = [
        MessageDTO(id="1", text="Hello", is_bot=False, conversation_id="conv1", rating=5, created_at="2024-01-01"),
        MessageDTO(id="2", text="How are you?", is_bot=False, conversation_id="conv1", rating=4, created_at="2024-01-02"),
    ]

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.return_value = messages_models

    result = get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    assert result is not None
    assert len(result) == 2
    assert result[0].get_id() == "1"
    assert result[1].get_id() == "2"

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_called_once()

def test_get_messages_by_conversation_exception(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    conversation_dto = MessageDTO(id=None, text=None, is_bot=None, conversation_id="conv1", rating=None, created_at=None)

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.side_effect = Exception("Errore nel recupero dei messaggi")

    with pytest.raises(Exception) as exc_info:
        get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    assert "Errore nel recupero dei messaggi" in str(exc_info.value)

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_called_once()
    
def test_get_messages_by_conversation_empty_dto(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    """Test per un DTO vuoto che verifica la gestione degli input non validi."""
    conversation_dto = MessageDTO(id=None, text=None, is_bot=None, conversation_id=None, rating=None, created_at=None)

    with pytest.raises(ValueError, match="Invalid conversation ID"):
        get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_not_called()
