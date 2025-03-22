from abc import ABC, abstractmethod
from models.message_model import MessageModel

class GetMessagesByConversationPort(ABC):
    """
    GetMessagesByConversationPort is an interface for getting messages by conversation ID.
    """

    @abstractmethod
    def get_messages_by_conversation(self, conversation_id: int) -> list[MessageModel]:
        """
        Get messages by conversation ID.
        Args:
            conversation_id (int): The ID of the conversation.
        Returns:
            list[MessageModel]: The list of message models.
        """
