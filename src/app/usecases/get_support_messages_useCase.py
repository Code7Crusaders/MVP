from abc import ABC, abstractmethod
from app.models.support_message_model import SupportMessageModel

class GetSupportMessagesUseCase(ABC):
    @abstractmethod
    def get_support_messages(self) -> list[SupportMessageModel]:
        pass
