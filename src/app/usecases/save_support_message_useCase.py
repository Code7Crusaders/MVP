from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class SaveSupportMessageUseCase(ABC):
    """
    Service class to handle support messages
    """

    @abstractmethod
    def save_support_message(self, support_message: SupportMessageModel)-> int:
        """
        Save a support message.
        Args:
            support_message (SupportMessageModel): The support message to save.
        Returns:
            int: The ID of the saved support message.
        """
