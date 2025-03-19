from abc import ABC, abstractmethod
from app.models.conversation_model import ConversationModel

class GetConversationsUseCase(ABC):
    @abstractmethod
    def get_conversations(self) -> list[ConversationModel]:
        pass
