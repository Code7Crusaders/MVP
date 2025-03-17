from abc import ABC, abstractmethod
import app.models.support_message_model as SupportMessageModel

class GetSupportMessagePort(ABC):
    """
    GetSupportMessagePort is an interface for getting a support message by its ID.
    """

    @abstractmethod
    def get_support_message(self, message_id: int) -> SupportMessageModel:
        """
        Get a support message by its ID.
        Args:
            message_id (int): The ID of the support message.
        Returns:
            SupportMessageModel: The support message model.
        """
