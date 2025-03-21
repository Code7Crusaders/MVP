from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class SaveConversationTitlePort(ABC):
    """
    SaveConversationTitlePort is an interface for saving a conversation title by its ID.
    """

    @abstractmethod
    def save_conversation_title(self, conversation_id: int, title: str) -> ConversationModel:
        """
        Save a conversation title by its ID.
        Args:
            conversation_id (int): The ID of the conversation.
            title (str): The new title of the conversation.
        Returns:
            ConversationModel: The updated conversation model.
        """