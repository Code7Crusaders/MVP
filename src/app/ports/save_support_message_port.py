from abc import ABC, abstractmethod
import app.models.support_message_model as SupportMessageModel

class SaveSupportMessagePort(ABC):
    """
    SaveSupportMessagePort is an interface for saving a support message.
    """

    @abstractmethod
    def save_support_message(self, user_id: int, description: str, status: str, subject: str):
        """
        Save a support message.
        Args:
            user_id (int): The ID of the user.
            description (str): The description of the support message.
            status (str): The status of the support message.
            subject (str): The subject of the support message.
        """
        pass