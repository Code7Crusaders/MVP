import pytest
from unittest.mock import MagicMock
from services.get_messages_by_conversation_service import GetMessagesByConversationService
from models.message_model import MessageModel
from ports.get_messages_by_conversation_port import GetMessagesByConversationPort

@pytest.fixture
def get_messages_by_conversation_port_mock():
    """Fixture per il mock del port."""
    return MagicMock(spec=GetMessagesByConversationPort)

@pytest.fixture
def get_messages_by_conversation_service(get_messages_by_conversation_port_mock):
    """Fixture per l'istanza del servizio."""
    return GetMessagesByConversationService(get_messages_by_conversation_port=get_messages_by_conversation_port_mock)

def test_get_messages_by_conversation_success(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    """Test per verificare il recupero e l'ordinamento corretto dei messaggi."""
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)

    # Mock dei messaggi con valori di created_at validi
    messages = [
        MessageModel(id="msg_1", created_at="2023-01-01T10:00:00"),
        MessageModel(id="msg_2", created_at="2023-01-01T11:00:00"),
        MessageModel(id="msg_3", created_at="2023-01-01T09:00:00"),
    ]

    get_messages_by_conversation_port_mock.get_messages_by_conversation.return_value = messages

    result = get_messages_by_conversation_service.get_messages_by_conversation(conversation)

    # Verifica che i messaggi siano ordinati correttamente per created_at
    expected_result = sorted(messages, key=lambda message: message.get_created_at())
    assert result == expected_result
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)

def test_get_messages_by_conversation_empty_list(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    """Test per verificare il comportamento con una lista vuota di messaggi."""
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)
    
    # Mock per una lista vuota di messaggi
    get_messages_by_conversation_port_mock.get_messages_by_conversation.return_value = []

    result = get_messages_by_conversation_service.get_messages_by_conversation(conversation)

    assert result == []
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)

def test_get_messages_by_conversation_null_created_at(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    """Test per verificare il comportamento con valori di created_at nulli."""
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)

    # Mock dei messaggi con valori di created_at nulli
    messages = [
        MessageModel(id="msg_1", created_at=None),
        MessageModel(id="msg_2", created_at="2023-01-01T11:00:00"),
        MessageModel(id="msg_3", created_at=None),
    ]

    get_messages_by_conversation_port_mock.get_messages_by_conversation.return_value = messages

    result = get_messages_by_conversation_service.get_messages_by_conversation(conversation)

    # Verifica che i messaggi siano ordinati correttamente (None ordinato come valore minimo)
    expected_result = sorted(messages, key=lambda message: message.get_created_at() or "")
    assert result == expected_result
    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)

def test_get_messages_by_conversation_exception(get_messages_by_conversation_service, get_messages_by_conversation_port_mock):
    """Test per verificare il comportamento in caso di eccezione."""
    conversation_id = "conversation_123"
    conversation = MessageModel(id=conversation_id)

    # Mock che simula il lancio di un'eccezione
    get_messages_by_conversation_port_mock.get_messages_by_conversation.side_effect = Exception("Error retrieving messages")

    with pytest.raises(Exception, match="Error retrieving messages"):
        get_messages_by_conversation_service.get_messages_by_conversation(conversation)

    get_messages_by_conversation_port_mock.get_messages_by_conversation.assert_called_once_with(conversation)
