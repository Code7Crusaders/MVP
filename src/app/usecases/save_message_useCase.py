from abc import ABC, abstractmethod
from models.message_model import MessageModel

class SaveMessageUseCase(ABC):

    @abstractmethod
    def save_message(self, message: MessageModel)-> int:
        """
        Save a message.
        Args:
            message (MessageModel): The message model.
        Returns:
            int: The ID of the saved message.
        """
