from abc import ABC, abstractmethod
from app.models.message_model import MessageModel

class GetMessageUseCase(ABC):
    @abstractmethod
    def get_message(self, message_id: int) -> MessageModel:
        pass
