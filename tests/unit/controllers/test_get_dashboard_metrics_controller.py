import pytest
from unittest.mock import MagicMock
from controllers.get_dashboard_metrics_controller import GetDashboardMetricsController
from usecases.get_dashboard_metrics_useCase import GetDashboardMetricsUseCase
from dto.metrics_dto import MetricsDTO

@pytest.fixture
def mock_get_dashboard_metrics_use_case():
    return MagicMock(spec=GetDashboardMetricsUseCase)


@pytest.fixture
def get_dashboard_metrics_controller(mock_get_dashboard_metrics_use_case):
    return GetDashboardMetricsController(mock_get_dashboard_metrics_use_case)


@pytest.fixture
def mock_metrics_dto():
    mock_dto = MagicMock(spec=MetricsDTO)
    mock_dto.get_total_likes.return_value = 100
    mock_dto.get_total_dislikes.return_value = 20
    mock_dto.get_total_messages.return_value = 50
    mock_dto.get_positive_rating.return_value = 80.0
    return mock_dto


def test_get_dashboard_metrics_success(get_dashboard_metrics_controller, mock_get_dashboard_metrics_use_case, mock_metrics_dto):
    # Arrange
    mock_get_dashboard_metrics_use_case.get_dashboard_metrics.return_value = mock_metrics_dto

    # Act
    result = get_dashboard_metrics_controller.get_dashboard_metrics()

    # Assert
    assert isinstance(result, MetricsDTO)
    assert result.total_likes == 100
    assert result.total_dislikes == 20
    assert result.total_messages == 50
    assert result.positive_rating == 80.0
    mock_get_dashboard_metrics_use_case.get_dashboard_metrics.assert_called_once()


def test_get_dashboard_metrics_failure(get_dashboard_metrics_controller, mock_get_dashboard_metrics_use_case):
    # Arrange
    mock_get_dashboard_metrics_use_case.get_dashboard_metrics.side_effect = Exception("Metrics retrieval failed")

    # Act & Assert
    with pytest.raises(Exception, match="Metrics retrieval failed"):
        get_dashboard_metrics_controller.get_dashboard_metrics()
    mock_get_dashboard_metrics_use_case.get_dashboard_metrics.assert_called_once()