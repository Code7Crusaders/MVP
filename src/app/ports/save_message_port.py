from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class SaveMessagePort(ABC):
    """
    SaveMessagePort is an interface for saving a message.
    """

    @abstractmethod
    def save_message(self, message: MessageModel):
        """
        Save a message.
        Args:
            message (MessageModel): The message model.
        """
