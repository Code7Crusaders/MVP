from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class SaveMessageUseCase(ABC):
    @abstractmethod
    def save_message(self, message: MessageModel):
        pass
