import pytest
from unittest.mock import MagicMock
from controllers.get_support_messages_controller import GetSupportMessagesController
from usecases.get_support_messages_useCase import GetSupportMessagesUseCase
from dto.support_message_dto import SupportMessageDTO
from models.support_message_model import SupportMessageModel

@pytest.fixture
def get_support_messages_use_case_mock():
    return MagicMock(spec=GetSupportMessagesUseCase)

@pytest.fixture
def get_support_messages_controller(get_support_messages_use_case_mock):
    return GetSupportMessagesController(get_support_messages_use_case_mock)

def test_get_support_messages_valid(get_support_messages_controller, get_support_messages_use_case_mock):
    support_messages_models = [
        SupportMessageModel(id="1", user_id="123", description="Issue 1", status="Open", subject="Login Issue", created_at="2024-01-01"),
        SupportMessageModel(id="2", user_id="456", description="Issue 2", status="Closed", subject="Payment Issue", created_at="2024-01-02")
    ]

    # Simula il comportamento dell'use case
    get_support_messages_use_case_mock.get_support_messages.return_value = support_messages_models

    result = get_support_messages_controller.get_support_messages()

    assert len(result) == 2
    assert result[0].get_id() == "1"
    assert result[0].get_user_id() == "123"
    assert result[0].get_description() == "Issue 1"
    assert result[0].get_status() == "Open"
    assert result[0].get_subject() == "Login Issue"
    assert result[0].get_created_at() == "2024-01-01"

    assert result[1].get_id() == "2"
    assert result[1].get_user_id() == "456"
    assert result[1].get_description() == "Issue 2"
    assert result[1].get_status() == "Closed"
    assert result[1].get_subject() == "Payment Issue"
    assert result[1].get_created_at() == "2024-01-02"

    get_support_messages_use_case_mock.get_support_messages.assert_called_once()

def test_get_support_messages_empty(get_support_messages_controller, get_support_messages_use_case_mock):
    # Simula il caso in cui non ci siano messaggi di supporto
    get_support_messages_use_case_mock.get_support_messages.return_value = []

    result = get_support_messages_controller.get_support_messages()

    assert result == []
    get_support_messages_use_case_mock.get_support_messages.assert_called_once()

def test_get_support_messages_exception(get_support_messages_controller, get_support_messages_use_case_mock):
    # Simula un'eccezione generata dall'use case
    get_support_messages_use_case_mock.get_support_messages.side_effect = Exception("Errore nel recupero dei messaggi di supporto")

    with pytest.raises(Exception) as exc_info:
        get_support_messages_controller.get_support_messages()

    assert "Errore nel recupero dei messaggi di supporto" in str(exc_info.value)
    get_support_messages_use_case_mock.get_support_messages.assert_called_once()
