from abc import ABC, abstractmethod
from app.models.support_message_model import SupportMessageModel

class GetSupportMessageUseCase(ABC):
    @abstractmethod
    def get_support_message(self, message_id: int) -> SupportMessageModel:
        pass
