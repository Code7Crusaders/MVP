from abc import ABC, abstractmethod
from models.metrics_model import MetricsModel

class GetDashboardMetricsUseCase(ABC):

    @abstractmethod
    def get_dashboard_metrics(self) -> MetricsModel:
        """
        Get dashboard metrics.
        Returns:
            MetricsDTO: An object containing the dashboard metrics.
        """
        