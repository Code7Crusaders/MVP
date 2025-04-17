import pytest
from unittest.mock import Mock
from services.delete_conversation_service import DeleteConversationService
from models.conversation_model import ConversationModel
from ports.delete_conversation_port import DeleteConversationPort

@pytest.fixture
def mock_delete_conversation_port():
    return Mock(spec=DeleteConversationPort)

@pytest.fixture
def delete_conversation_service(mock_delete_conversation_port):
    return DeleteConversationService(delete_conversation_port=mock_delete_conversation_port)

@pytest.fixture
def sample_conversation():
    return ConversationModel(id=1, title="Sample Conversation")

def test_delete_conversation_success(delete_conversation_service, mock_delete_conversation_port, sample_conversation):
    # Arrange
    mock_delete_conversation_port.delete_conversation_title.return_value = True

    # Act
    result = delete_conversation_service.delete_conversation(sample_conversation)

    # Assert
    assert result is True
    mock_delete_conversation_port.delete_conversation_title.assert_called_once_with(sample_conversation)

def test_delete_conversation_failure(delete_conversation_service, mock_delete_conversation_port, sample_conversation):
    # Arrange
    mock_delete_conversation_port.delete_conversation_title.return_value = False

    # Act
    result = delete_conversation_service.delete_conversation(sample_conversation)

    # Assert
    assert result is False
    mock_delete_conversation_port.delete_conversation_title.assert_called_once_with(sample_conversation)

def test_delete_conversation_exception(delete_conversation_service, mock_delete_conversation_port, sample_conversation):
    # Arrange
    mock_delete_conversation_port.delete_conversation_title.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(Exception, match="Database error"):
        delete_conversation_service.delete_conversation(sample_conversation)
    mock_delete_conversation_port.delete_conversation_title.assert_called_once_with(sample_conversation)