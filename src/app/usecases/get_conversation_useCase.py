from abc import ABC, abstractmethod
from app.models.conversation_model import ConversationModel

class GetConversationUseCase(ABC):
    @abstractmethod
    def get_conversation_answer(self, conversation_id: int) -> ConversationModel:
        pass

