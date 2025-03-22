from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class GetMessageUseCase(ABC):
    
    @abstractmethod
    def get_message(self, message: MessageModel) -> MessageModel:
        """
        Retrieve a message by its ID.
        Args:
            message (MessageModel): The message object containing the ID to retrieve.
        Returns:
            MessageModel: The retrieved message.
        """
