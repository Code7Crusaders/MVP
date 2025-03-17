from abc import ABC, abstractmethod
import app.models.conversation_model as ConversationModel

class GetConversationPort(ABC):
    """
    GetConversationPort is an interface for getting a conversation by its ID.
    """

    @abstractmethod
    def get_conversation(self, conversation_id: int) -> ConversationModel:
        """
        Get a conversation by its ID.
        Args:
            conversation_id (int): The ID of the conversation.
        Returns:
            ConversationModel: The conversation model.
        """
        