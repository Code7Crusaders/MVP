import pytest
from unittest.mock import MagicMock
from controllers.get_message_controller import GetMessageController
from usecases.get_message_useCase import GetMessageUseCase
from dto.message_dto import MessageDTO
from models.message_model import MessageModel

@pytest.fixture
def get_message_use_case_mock():
    return MagicMock(spec=GetMessageUseCase)

@pytest.fixture
def get_message_controller(get_message_use_case_mock):
    return GetMessageController(get_message_use_case_mock)

# Test get_message

def test_get_message_valid(get_message_controller, get_message_use_case_mock):
    message_dto = MessageDTO(id="1", text="Hello", is_bot=False, conversation_id="456", rating=5, created_at="2024-01-01")
    message_model = MessageModel(id="1", text="Hello", is_bot=False, conversation_id="456", rating=5, created_at="2024-01-01")

    get_message_use_case_mock.get_message.return_value = message_model

    result = get_message_controller.get_message(message_dto)

    assert result is not None
    assert result.get_id() == "1"
    assert result.get_text() == "Hello"
    assert result.get_is_bot() == False
    assert result.get_conversation_id() == "456"
    assert result.get_rating() == 5
    assert result.get_created_at() == "2024-01-01"

    get_message_use_case_mock.get_message.assert_called_once()

def test_get_message_not_found(get_message_controller, get_message_use_case_mock):
    message_dto = MessageDTO(id="1", text="Hello", is_bot=False, conversation_id="456", rating=5, created_at="2024-01-01")

    get_message_use_case_mock.get_message.return_value = None

    result = get_message_controller.get_message(message_dto)

    assert result is None
    get_message_use_case_mock.get_message.assert_called_once()

def test_get_message_exception(get_message_controller, get_message_use_case_mock):
    message_dto = MessageDTO(id="1", text="Hello", is_bot=False, conversation_id="456", rating=5, created_at="2024-01-01")

    get_message_use_case_mock.get_message.side_effect = Exception("Errore nel recupero del messaggio")

    with pytest.raises(Exception) as exc_info:
        get_message_controller.get_message(message_dto)

    assert "Errore nel recupero del messaggio" in str(exc_info.value)
    get_message_use_case_mock.get_message.assert_called_once()
