from abc import ABC, abstractmethod
from app.models.conversation_model import ConversationModel

class GetConversationPort(ABC):
    """
    GetConversationPort is an interface for getting a conversation by its ID.
    """

    @abstractmethod
    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        Get a conversation by its model.
        Args:
            conversation (ConversationModel): The conversation model.
        Returns:
            ConversationModel: The conversation model.
        """
        pass
        