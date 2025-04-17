import pytest
from unittest.mock import Mock
from services.mark_done_support_message_services import MarkDoneSupportMessagesService
from models.support_message_model import SupportMessageModel
from ports.mark_done_support_messages_port import MarkDoneSupportMessagesPort

@pytest.fixture
def mock_mark_done_support_messages_port():
    return Mock(spec=MarkDoneSupportMessagesPort)

@pytest.fixture
def mark_done_support_messages_service(mock_mark_done_support_messages_port):
    return MarkDoneSupportMessagesService(mark_done_support_messages_port=mock_mark_done_support_messages_port)

def test_mark_done_support_message_success(mark_done_support_messages_service, mock_mark_done_support_messages_port):
    # Arrange
    mock_mark_done_support_messages_port.mark_done_support_messages.return_value = 1

    support_model = SupportMessageModel(
        id=1,
        user_id=1,
        user_email="test@example.com",
        description="Test description",
        status="true",
        subject="Test subject",
        created_at="2023-10-01T00:00:00Z",
    )

    # Act
    result = mark_done_support_messages_service.mark_done_support_messages(support_model)

    # Assert
    assert result == 1

def test_mark_done_support_message_no_changes(mark_done_support_messages_service, mock_mark_done_support_messages_port):
    # Arrange
    mock_mark_done_support_messages_port.mark_done_support_messages.return_value = 0

    support_model = SupportMessageModel(
        id=2,
        user_id=2,
        user_email="user2@example.com",
        description="Another test description",
        status="false",
        subject="Another test subject",
        created_at="2023-10-02T00:00:00Z",
    )

    # Act
    result = mark_done_support_messages_service.mark_done_support_messages(support_model)

    # Assert
    assert result == 0
    mock_mark_done_support_messages_port.mark_done_support_messages.assert_called_once_with(support_model)

def test_mark_done_support_message_exception(mark_done_support_messages_service, mock_mark_done_support_messages_port):
    # Arrange
    mock_mark_done_support_messages_port.mark_done_support_messages.side_effect = Exception("Database error")

    support_model = SupportMessageModel(
        id=3,
        user_id=3,
        user_email="user3@example.com",
        description="Exception test description",
        status="pending",
        subject="Exception test subject",
        created_at="2023-10-03T00:00:00Z",
    )

    # Act & Assert
    with pytest.raises(Exception, match="Database error"):
        mark_done_support_messages_service.mark_done_support_messages(support_model)
    mock_mark_done_support_messages_port.mark_done_support_messages.assert_called_once_with(support_model)