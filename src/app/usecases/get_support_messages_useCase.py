from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class GetSupportMessagesUseCase(ABC):

    @abstractmethod
    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Retrieves all support messages.
        Returns:
            list[SupportMessageModel]: A list of support messages.
        """
