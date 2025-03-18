from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class GetMessagesByConversationUseCase(ABC):
    @abstractmethod
    def get_messages_by_conversation(self, conversation_id: int) -> list[MessageModel]:
        pass
