from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class GetConversationUseCase(ABC):
    
    @abstractmethod
    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        get the conversation title from db using id to get it.
        Args:
            conversation (ConversationModel): The conversation to be retrieved.
        Returns:
            ConversationModel: The conversation retrieved from db.
        """

