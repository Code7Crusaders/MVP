import pytest
from unittest.mock import MagicMock
from controllers.mark_done_support_message_contoller import MarkDoneSupportMessagesController
from usecases.mark_done_support_messages_useCase import MarkDoneSupportMessagesUseCase
from dto.support_message_dto import SupportMessageDTO

@pytest.fixture
def mock_mark_done_support_messages_use_case():
    return MagicMock(spec=MarkDoneSupportMessagesUseCase)


@pytest.fixture
def mark_done_support_messages_controller(mock_mark_done_support_messages_use_case):
    return MarkDoneSupportMessagesController(mock_mark_done_support_messages_use_case)


@pytest.fixture
def mock_support_message_dto():
    mock_dto = MagicMock(spec=SupportMessageDTO)
    mock_dto.get_id.return_value = 1
    mock_dto.get_status.return_value = "done"
    return mock_dto


def test_mark_done_support_messages_success(mark_done_support_messages_controller, mock_mark_done_support_messages_use_case, mock_support_message_dto):
    # Arrange
    mock_mark_done_support_messages_use_case.mark_done_support_messages.return_value = 1

    # Act
    result = mark_done_support_messages_controller.mark_done_support_messages(mock_support_message_dto)

    # Assert
    assert result == 1
    mock_mark_done_support_messages_use_case.mark_done_support_messages.assert_called_once()


def test_mark_done_support_messages_failure(mark_done_support_messages_controller, mock_mark_done_support_messages_use_case, mock_support_message_dto):
    # Arrange
    mock_mark_done_support_messages_use_case.mark_done_support_messages.return_value = 0

    # Act
    result = mark_done_support_messages_controller.mark_done_support_messages(mock_support_message_dto)

    # Assert
    assert result == 0
    mock_mark_done_support_messages_use_case.mark_done_support_messages.assert_called_once()


def test_mark_done_support_messages_raises_exception(mark_done_support_messages_controller, mock_mark_done_support_messages_use_case, mock_support_message_dto):
    # Arrange
    mock_mark_done_support_messages_use_case.mark_done_support_messages.side_effect = Exception("Marking failed")

    # Act & Assert
    with pytest.raises(Exception, match="Marking failed"):
        mark_done_support_messages_controller.mark_done_support_messages(mock_support_message_dto)
    mock_mark_done_support_messages_use_case.mark_done_support_messages.assert_called_once()