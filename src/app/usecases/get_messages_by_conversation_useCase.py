from abc import ABC, abstractmethod
from models.message_model import MessageModel

class GetMessagesByConversationUseCase(ABC):
    
    @abstractmethod
    def get_messages_by_conversation(self, conversation: MessageModel) -> list[MessageModel]:
        """
        Retrieve messages by conversation.
        Args:
            conversation (MessageModel): The conversation object containing the ID to retrieve messages for.
        Returns:
            list[MessageModel]: A list of retrieved messages.
        """
