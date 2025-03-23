import pytest
from unittest.mock import MagicMock
from controllers.get_support_message_controller import GetSupportMessageController
from usecases.get_support_message_useCase import GetSupportMessageUseCase
from dto.support_message_dto import SupportMessageDTO
from models.support_message_model import SupportMessageModel

@pytest.fixture
def get_support_message_use_case_mock():
    return MagicMock(spec=GetSupportMessageUseCase)

@pytest.fixture
def get_support_message_controller(get_support_message_use_case_mock):
    return GetSupportMessageController(get_support_message_use_case_mock)

def test_get_support_message_valid(get_support_message_controller, get_support_message_use_case_mock):
    support_message_dto = SupportMessageDTO(
        id="1", user_id="123", description="Issue with login", status="Open", 
        subject="Login Issue", created_at="2024-01-01"
    )
    
    support_message_model = SupportMessageModel(
        id="1", user_id="123", description="Issue with login", status="Open", 
        subject="Login Issue", created_at="2024-01-01"
    )

    # Simula il comportamento dell'use case
    get_support_message_use_case_mock.get_support_message.return_value = support_message_model

    result = get_support_message_controller.get_support_message(support_message_dto)

    assert result is not None
    assert result.get_id() == "1"
    assert result.get_user_id() == "123"
    assert result.get_description() == "Issue with login"
    assert result.get_status() == "Open"
    assert result.get_subject() == "Login Issue"
    assert result.get_created_at() == "2024-01-01"

    get_support_message_use_case_mock.get_support_message.assert_called_once()

def test_get_support_message_not_found(get_support_message_controller, get_support_message_use_case_mock):
    support_message_dto = SupportMessageDTO(
        id="1", user_id="123", description="Issue with login", status="Open", 
        subject="Login Issue", created_at="2024-01-01"
    )

    # Simula il caso in cui il messaggio di supporto non viene trovato
    get_support_message_use_case_mock.get_support_message.return_value = None

    result = get_support_message_controller.get_support_message(support_message_dto)

    assert result is None
    get_support_message_use_case_mock.get_support_message.assert_called_once()

def test_get_support_message_exception(get_support_message_controller, get_support_message_use_case_mock):
    support_message_dto = SupportMessageDTO(
        id="1", user_id="123", description="Issue with login", status="Open", 
        subject="Login Issue", created_at="2024-01-01"
    )

    # Simula un'eccezione generata dall'use case
    get_support_message_use_case_mock.get_support_message.side_effect = Exception("Errore nel recupero del messaggio di supporto")

    with pytest.raises(Exception) as exc_info:
        get_support_message_controller.get_support_message(support_message_dto)

    assert "Errore nel recupero del messaggio di supporto" in str(exc_info.value)
    get_support_message_use_case_mock.get_support_message.assert_called_once()
