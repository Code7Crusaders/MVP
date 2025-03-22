from abc import ABC, abstractmethod
import models.support_message_model as SupportMessageModel

class SaveSupportMessagePort(ABC):
    """
    SaveSupportMessagePort is an interface for saving a support message.
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