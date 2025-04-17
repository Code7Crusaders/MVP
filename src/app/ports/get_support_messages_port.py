from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class GetSupportMessagesPort(ABC):
    """
    GetSupportMessagePort is an interface for getting all support messages.
    """

    @abstractmethod
    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Retrieves all support messages.
        Returns:
            list[SupportMessageModel]: A list of support messages.
        """
