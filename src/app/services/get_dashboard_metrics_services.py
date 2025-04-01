from abc import ABC
from models.metrics_model import MetricsModel
from usecases.get_dashboard_metrics_useCase import GetDashboardMetricsUseCase
from ports.get_all_messages_port import GetAllMessagesPort

class GetDashboardMetricsService(GetDashboardMetricsUseCase):
    def __init__(self, get_all_messages_port: GetAllMessagesPort):
        self.get_all_messages_port = get_all_messages_port

    def get_dashboard_metrics(self) -> MetricsModel:
        """
        Get dashboard metrics.
        Returns:
            MetricsModel: An object containing the dashboard metrics.
        """
        try:
            messages = self.get_all_messages_port.fetch_messages()

            total_likes = 0
            total_dislikes = 0
            total_messages = len(messages)
            rated_messages_count = 0  
            positive_rating = 0

            for message in messages:
                rating = message.get_rating()
                if rating is not None:  
                    rated_messages_count += 1
                    if rating == True:
                        total_likes += 1
                    elif rating == False:
                        total_dislikes += 1

            if rated_messages_count > 0:
                positive_rating = (total_likes / rated_messages_count) * 100

            return MetricsModel(
                total_likes=total_likes,
                total_dislikes=total_dislikes,
                total_messages=total_messages,
                positive_rating=positive_rating
            )

        except Exception as e:
            raise e
