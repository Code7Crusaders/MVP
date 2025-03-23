import pytest
from unittest.mock import MagicMock
from controllers.save_support_message_controller import SaveSupportMessageController
from usecases.save_support_message_useCase import SaveSupportMessageUseCase
from dto.support_message_dto import SupportMessageDTO
from models.support_message_model import SupportMessageModel

@pytest.fixture
def save_support_message_use_case_mock():
    return MagicMock(spec=SaveSupportMessageUseCase)

@pytest.fixture
def save_support_message_controller(save_support_message_use_case_mock):
    return SaveSupportMessageController(save_support_message_use_case_mock)

def test_save_support_message_valid(save_support_message_controller, save_support_message_use_case_mock):
    support_message_dto = SupportMessageDTO(
        id="1",
        user_id="123",
        description="Issue description",
        status="Open",
        subject="Login Issue",
        created_at="2024-01-01"
    )

    # Simula il comportamento dell'use case per restituire un ID
    save_support_message_use_case_mock.save_support_message.return_value = 1

    result = save_support_message_controller.save_support_message(support_message_dto)

    assert result == 1
    save_support_message_use_case_mock.save_support_message.assert_called_once()

def test_save_support_message_exception(save_support_message_controller, save_support_message_use_case_mock):
    support_message_dto = SupportMessageDTO(
        id="1",
        user_id="123",
        description="Issue description",
        status="Open",
        subject="Login Issue",
        created_at="2024-01-01"
    )

    # Simula un'eccezione generata dall'use case
    save_support_message_use_case_mock.save_support_message.side_effect = Exception("Errore durante il salvataggio del messaggio di supporto")

    with pytest.raises(Exception) as exc_info:
        save_support_message_controller.save_support_message(support_message_dto)

    assert "Errore durante il salvataggio del messaggio di supporto" in str(exc_info.value)
    save_support_message_use_case_mock.save_support_message.assert_called_once()
