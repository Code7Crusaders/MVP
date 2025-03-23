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

def test_get_messages_by_conversation_valid(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    conversation_dto = MessageDTO(id="conv1", text=None, user_id=None, conversation_id="conv1", rating=None, created_at=None)

    messages_models = [
        MessageDTO(id="1", text="Hello", user_id="123", conversation_id="conv1", rating=5, created_at="2024-01-01"),
        MessageDTO(id="2", text="How are you?", user_id="456", conversation_id="conv1", rating=4, created_at="2024-01-02"),
    ]

    # Simula il comportamento dell'use case
    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.return_value = messages_models

    result = get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    assert result is not None
    assert len(result) == 2
    assert result[0].get_id() == "1"
    assert result[1].get_id() == "2"

    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_called_once()

def test_get_messages_by_conversation_not_found(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    conversation_dto = MessageDTO(id="conv1", text=None, user_id=None, conversation_id="conv1", rating=None, created_at=None)

    # Simula il caso in cui non ci sono messaggi nella conversazione
    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.return_value = []

    result = get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    assert result is None
    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_called_once()

def test_get_messages_by_conversation_exception(get_messages_by_conversation_controller, get_messages_by_conversation_use_case_mock):
    conversation_dto = MessageDTO(id="conv1", text=None, user_id=None, conversation_id="conv1", rating=None, created_at=None)

    # Simula un'eccezione generata dall'use case
    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.side_effect = Exception("Errore nel recupero dei messaggi")

    with pytest.raises(Exception) as exc_info:
        get_messages_by_conversation_controller.get_messages_by_conversation(conversation_dto)

    assert "Errore nel recupero dei messaggi" in str(exc_info.value)
    get_messages_by_conversation_use_case_mock.get_messages_by_conversation.assert_called_once()
