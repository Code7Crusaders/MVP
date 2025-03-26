import pytest
from unittest.mock import MagicMock
from controllers.save_message_controller import SaveMessageController
from usecases.save_message_useCase import SaveMessageUseCase
from dto.message_dto import MessageDTO
from models.message_model import MessageModel

@pytest.fixture
def save_message_use_case_mock():
    return MagicMock(spec=SaveMessageUseCase)

@pytest.fixture
def save_message_controller(save_message_use_case_mock):
    return SaveMessageController(save_message_use_case_mock)

# Test save_message

def test_save_message_valid(save_message_controller, save_message_use_case_mock):
    message_dto = MessageDTO(id=None, text="Hello", is_bot=False, conversation_id="conv1", rating=5, created_at="2024-01-01")

    # Simula il comportamento dell'use case restituendo un ID fittizio
    save_message_use_case_mock.save_message.return_value = 1

    result = save_message_controller.save_message(message_dto)

    assert result == 1, "Il messaggio non è stato salvato correttamente"
    save_message_use_case_mock.save_message.assert_called_once()

def test_save_message_exception(save_message_controller, save_message_use_case_mock):
    message_dto = MessageDTO(id=None, text="Hello", is_bot=False, conversation_id="conv1", rating=5, created_at="2024-01-01")

    # Simula un'eccezione generata dall'use case
    save_message_use_case_mock.save_message.side_effect = Exception("Errore nel salvataggio del messaggio")

    with pytest.raises(Exception) as exc_info:
        save_message_controller.save_message(message_dto)

    assert "Errore nel salvataggio del messaggio" in str(exc_info.value)
    save_message_use_case_mock.save_message.assert_called_once()
