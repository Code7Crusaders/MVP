
from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class DeleteConversationPort(ABC):

    @abstractmethod
    def delete_conversation_title(self, conversation: ConversationModel) -> bool:
        """
        Delete a conversation title.
        Args:
            conversation (ConversationModel): The conversation object containing the ID to delete.
        Returns:
            int: The ID of the deleted conversation.
        """