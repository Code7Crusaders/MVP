from usecases.get_dashboard_metrics_useCase import GetDashboardMetricsUseCase
from dto.metrics_dto import MetricsDTO
from models.message_model import MessageModel

class GetDashboardMetricsController:

    def __init__(self, get_dashboard_metrics_use_case: GetDashboardMetricsUseCase):
        self.get_dashboard_metrics_use_case = get_dashboard_metrics_use_case

    def get_dashboard_metrics(self) -> MetricsDTO:
        """
        Get dashboard metrics.
        Returns:
            MetricsDTO: An object containing the dashboard metrics.
        """
        try:
            metrics_result = self.get_dashboard_metrics_use_case.get_dashboard_metrics()

            return MetricsDTO(
                total_likes=metrics_result.get_total_likes(),
                total_dislikes=metrics_result.get_total_dislikes(),
                total_messages=metrics_result.get_total_dislikes(),
                positive_rating=metrics_result.get_positive_rating()
            )

        except Exception as e:
            raise e