from abc import ABC, abstractmethod
from app.models.conversation_model import ConversationModel

class GetConversationUseCase(ABC):
    @abstractmethod
    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        pass

