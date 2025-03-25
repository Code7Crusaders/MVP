from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class GetConversationsUseCase(ABC):

    @abstractmethod
    def get_conversations(self, user_id : int) -> list[ConversationModel]:
        """
        Get all conversations.
        Returns:
            List[ConversationModel]: A list of conversation models.
        """
