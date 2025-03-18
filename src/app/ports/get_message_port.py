from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class GetMessagePort(ABC):
    """
    GetMessagePort is an interface for getting a message by its ID.
    """

    @abstractmethod
    def get_message(self, message_id: int) -> MessageModel:
        """
        Get a message by its ID.
        Args:
            message_id (int): The ID of the message.
        Returns:
            MessageModel: The message model.
        """
