import pytest
from unittest.mock import Mock
from services.get_dashboard_metrics_services import GetDashboardMetricsService
from models.metrics_model import MetricsModel
from ports.get_all_messages_port import GetAllMessagesPort
from models.message_model import MessageModel

@pytest.fixture
def mock_get_all_messages_port():
    return Mock(spec=GetAllMessagesPort)

@pytest.fixture
def get_dashboard_metrics_service(mock_get_all_messages_port):
    return GetDashboardMetricsService(get_all_messages_port=mock_get_all_messages_port)

@pytest.fixture
def sample_messages():
    return [
        Mock(get_rating=Mock(return_value=True)),  # Liked message
        Mock(get_rating=Mock(return_value=False)),  # Disliked message
        Mock(get_rating=Mock(return_value=None)),  # Unrated message
        Mock(get_rating=Mock(return_value=True)),  # Liked message
    ]

def test_get_dashboard_metrics_success(get_dashboard_metrics_service, mock_get_all_messages_port, sample_messages):
    # Arrange
    mock_get_all_messages_port.fetch_messages.return_value = sample_messages

    # Act
    metrics = get_dashboard_metrics_service.get_dashboard_metrics()

    # Assert
    assert isinstance(metrics, MetricsModel)
    assert metrics.total_likes == 2
    assert metrics.total_dislikes == 1
    assert metrics.total_messages == 4
    assert metrics.positive_rating == 66.66666666666666  # 2 out of 3 rated messages are positive
    mock_get_all_messages_port.fetch_messages.assert_called_once()

def test_get_dashboard_metrics_no_messages(get_dashboard_metrics_service, mock_get_all_messages_port):
    # Arrange
    mock_get_all_messages_port.fetch_messages.return_value = []

    # Act
    metrics = get_dashboard_metrics_service.get_dashboard_metrics()

    # Assert
    assert isinstance(metrics, MetricsModel)
    assert metrics.total_likes == 0
    assert metrics.total_dislikes == 0
    assert metrics.total_messages == 0
    assert metrics.positive_rating == 0
    mock_get_all_messages_port.fetch_messages.assert_called_once()

def test_get_dashboard_metrics_exception(get_dashboard_metrics_service, mock_get_all_messages_port):
    # Arrange
    mock_get_all_messages_port.fetch_messages.side_effect = Exception("Database error")

    # Act & Assert
    with pytest.raises(Exception, match="Database error"):
        get_dashboard_metrics_service.get_dashboard_metrics()
    mock_get_all_messages_port.fetch_messages.assert_called_once()

def test_get_dashboard_metrics_mixed_ratings(get_dashboard_metrics_service, mock_get_all_messages_port):
    # Arrange
    sample_messages = [
        MessageModel(
            id=1,
            text="Message 1",
            is_bot=False,
            conversation_id=101,
            rating=True,
            created_at="2023-01-01T10:00:00"
        ),
        MessageModel(
            id=2,
            text="Message 2",
            is_bot=False,
            conversation_id=102,
            rating=False,
            created_at="2023-01-02T11:00:00"
        ),
        MessageModel(
            id=3,
            text="Message 3",
            is_bot=False,
            conversation_id=103,
            rating=None,
            created_at="2023-01-03T12:00:00"
        ),
        MessageModel(
            id=4,
            text="Message 4",
            is_bot=False,
            conversation_id=104,
            rating=True,
            created_at="2023-01-04T13:00:00"
        ),
    ]
    mock_get_all_messages_port.fetch_messages.return_value = sample_messages

    # Act
    metrics = get_dashboard_metrics_service.get_dashboard_metrics()

    # Assert
    assert isinstance(metrics, MetricsModel)
    assert metrics.total_likes == 2
    assert metrics.total_dislikes == 1
    assert metrics.total_messages == 4
    assert metrics.positive_rating == 66.66666666666666  # 2 out of 3 rated messages are positive
    mock_get_all_messages_port.fetch_messages.assert_called_once()

def test_get_dashboard_metrics_all_dislikes(get_dashboard_metrics_service, mock_get_all_messages_port):
    # Arrange
    sample_messages = [
        MessageModel(
            id=1,
            text="Message 1",
            is_bot=False,
            conversation_id=101,
            rating=False,
            created_at="2023-01-01T10:00:00"
        ),
        MessageModel(
            id=2,
            text="Message 2",
            is_bot=False,
            conversation_id=102,
            rating=False,
            created_at="2023-01-02T11:00:00"
        ),
    ]
    mock_get_all_messages_port.fetch_messages.return_value = sample_messages

    # Act
    metrics = get_dashboard_metrics_service.get_dashboard_metrics()

    # Assert
    assert isinstance(metrics, MetricsModel)
    assert metrics.total_likes == 0  # No likes
    assert metrics.total_dislikes == 2  # Two dislikes
    assert metrics.total_messages == 2  # Total messages
    assert metrics.positive_rating == 0  # No positive ratings
    mock_get_all_messages_port.fetch_messages.assert_called_once()

def test_get_dashboard_metrics_mixed_ratings_with_dislikes(get_dashboard_metrics_service, mock_get_all_messages_port):
    # Arrange
    sample_messages = [
        Mock(get_rating=Mock(return_value=True)),   # Liked message
        Mock(get_rating=Mock(return_value=False)),  # Disliked message
        Mock(get_rating=Mock(return_value=None)),   # Unrated message
        Mock(get_rating=Mock(return_value=False)),  # Disliked message
    ]
    mock_get_all_messages_port.fetch_messages.return_value = sample_messages

    # Act
    metrics = get_dashboard_metrics_service.get_dashboard_metrics()

    # Assert
    assert isinstance(metrics, MetricsModel)
    assert metrics.total_likes == 1
    assert metrics.total_dislikes == 2
    assert metrics.total_messages == 4
    assert metrics.positive_rating == 33.33333333333333  # 1 out of 3 rated messages is positive
    mock_get_all_messages_port.fetch_messages.assert_called_once()