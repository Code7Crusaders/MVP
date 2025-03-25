from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class GetConversationsPort(ABC):
    """
    GetConversationsPort is an interface for getting multiple conversations.
    """

    @abstractmethod
    def get_conversations(self, user_id : int) -> list[ConversationModel]:
        """
        Get all conversations.
        Returns:
            List[ConversationModel]: A list of conversation models.
        """
