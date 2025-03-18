from abc import ABC, abstractmethod
from app.models.support_message_model import SupportMessageModel

class GetSupportMessagesPort(ABC):
    """
    GetSupportMessagePort is an interface for getting all support messages.
    """

    @abstractmethod
    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Returns:
            list of SupportMessageModel: The support message model .
        """
