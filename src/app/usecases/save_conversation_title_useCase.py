from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class SaveConversationTitleUseCase(ABC):

    @abstractmethod
    def save_conversation_title(self, conversation: ConversationModel) -> int:
        """
        Save a conversation title by its ID.
        Args:
            conversation (ConversationModel): The conversation model containing the ID and title.
        Returns:
            int: The ID of the updated conversation.
        """
 