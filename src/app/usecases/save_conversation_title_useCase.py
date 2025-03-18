from abc import ABC, abstractmethod

class SaveConversationTitleUseCase(ABC):
    @abstractmethod
    def save_conversation_title(self, conversation_id: int, title: str):
        pass
 