import pytest
from unittest.mock import MagicMock
from controllers.delete_conversation_controller import DeleteConversationController
from dto.conversation_dto import ConversationDTO
from usecases.delete_conversation_useCase import DeleteConversationUseCase

@pytest.fixture
def mock_delete_conversation_use_case():
    return MagicMock(spec=DeleteConversationUseCase)


@pytest.fixture
def delete_conversation_controller(mock_delete_conversation_use_case):
    return DeleteConversationController(mock_delete_conversation_use_case)


@pytest.fixture
def mock_conversation_dto():
    mock_dto = MagicMock(spec=ConversationDTO)
    mock_dto.get_id.return_value = 1
    mock_dto.get_title.return_value = "Test Conversation"
    mock_dto.get_user_id.return_value = 123
    return mock_dto


def test_delete_conversation_success(delete_conversation_controller, mock_delete_conversation_use_case, mock_conversation_dto):
    # Arrange
    mock_delete_conversation_use_case.delete_conversation.return_value = True

    # Act
    result = delete_conversation_controller.delete_conversation(mock_conversation_dto)

    # Assert
    assert result is True
    mock_delete_conversation_use_case.delete_conversation.assert_called_once()


def test_delete_conversation_failure(delete_conversation_controller, mock_delete_conversation_use_case, mock_conversation_dto):
    # Arrange
    mock_delete_conversation_use_case.delete_conversation.return_value = False

    # Act
    result = delete_conversation_controller.delete_conversation(mock_conversation_dto)

    # Assert
    assert result is False
    mock_delete_conversation_use_case.delete_conversation.assert_called_once()


def test_delete_conversation_raises_exception(delete_conversation_controller, mock_delete_conversation_use_case, mock_conversation_dto):
    # Arrange
    mock_delete_conversation_use_case.delete_conversation.side_effect = Exception("Deletion failed")

    # Act & Assert
    with pytest.raises(Exception, match="Deletion failed"):
        delete_conversation_controller.delete_conversation(mock_conversation_dto)
    mock_delete_conversation_use_case.delete_conversation.assert_called_once()