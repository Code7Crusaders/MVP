import pytest
from unittest.mock import Mock
from services.update_message_rating_service import UpdateMessageRatingService
from models.message_model import MessageModel
from ports.update_message_rating_port import UpdateMessageRatingPort

@pytest.fixture
def mock_update_message_rating_port():
    return Mock(spec=UpdateMessageRatingPort)

@pytest.fixture
def update_message_rating_service(mock_update_message_rating_port):
    return UpdateMessageRatingService(update_message_rating_port=mock_update_message_rating_port)

def test_update_message_rating_success(update_message_rating_service, mock_update_message_rating_port):
    # Arrange
    mock_update_message_rating_port.update_message_rating.return_value = True

    message_model = MessageModel(
        id=1,
        text="Test message",
        is_bot=False,
        conversation_id=101,
        rating=5,
        created_at="2023-10-01T00:00:00Z"
    )

    # Act
    result = update_message_rating_service.update_message_rating(message_model)

    # Assert
    assert result is True
    mock_update_message_rating_port.update_message_rating.assert_called_once_with(message_model)

def test_update_message_rating_failure(update_message_rating_service, mock_update_message_rating_port):
    # Arrange
    mock_update_message_rating_port.update_message_rating.return_value = False

    message_model = MessageModel(
        id=2,
        text="Another test message",
        is_bot=True,
        conversation_id=102,
        rating=3,
        created_at="2023-10-02T00:00:00Z"
    )

    # Act
    result = update_message_rating_service.update_message_rating(message_model)

    # Assert
    assert result is False
    mock_update_message_rating_port.update_message_rating.assert_called_once_with(message_model)

def test_update_message_rating_exception(update_message_rating_service, mock_update_message_rating_port):
    # Arrange
    mock_update_message_rating_port.update_message_rating.side_effect = Exception("Database error")

    message_model = MessageModel(
        id=3,
        text="Exception test message",
        is_bot=False,
        conversation_id=103,
        rating=4,
        created_at="2023-10-03T00:00:00Z"
    )

    # Act & Assert
    with pytest.raises(Exception, match="Database error"):
        update_message_rating_service.update_message_rating(message_model)
    mock_update_message_rating_port.update_message_rating.assert_called_once_with(message_model)