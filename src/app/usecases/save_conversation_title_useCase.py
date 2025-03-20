from abc import ABC, abstractmethod
from app.models.conversation_model import ConversationModel

class SaveConversationTitleUseCase(ABC):
    @abstractmethod
    def save_conversation_title(self, conversation: ConversationModel) -> bool:
        pass
 