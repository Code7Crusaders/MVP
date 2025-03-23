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

def test_save_message_valid(save_message_controller, save_message_use_case_mock):
    message_dto = MessageDTO(
        id="1",
        text="Hello World",
        user_id="123",
        conversation_id="456",
        rating=5,
        created_at="2024-01-01"
    )

    # Simula il comportamento dell'use case per restituire un ID
    save_message_use_case_mock.save_message.return_value = 1

    result = save_message_controller.save_message(message_dto)

    assert result == 1
    save_message_use_case_mock.save_message.assert_called_once()
    
def test_save_message_exception(save_message_controller, save_message_use_case_mock):
    message_dto = MessageDTO(
        id="1",
        text="Hello World",
        user_id="123",
        conversation_id="456",
        rating=5,
        created_at="2024-01-01"
    )

    # Simula un'eccezione generata dall'use case
    save_message_use_case_mock.save_message.side_effect = Exception("Errore durante il salvataggio")

    with pytest.raises(Exception) as exc_info:
        save_message_controller.save_message(message_dto)

    assert "Errore durante il salvataggio" in str(exc_info.value)
    save_message_use_case_mock.save_message.assert_called_once()
