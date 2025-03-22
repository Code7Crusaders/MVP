from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class GetSupportMessagePort(ABC):
    """
    GetSupportMessagePort is an interface for getting a support message by its ID.
    """

    @abstractmethod
    def get_support_message(self, message: SupportMessageModel) -> SupportMessageModel:
        """
        Retrieves a support message.
        Args:
            message (SupportMessageModel): The support message model containing the details.
        Returns:
            SupportMessageModel: The retrieved support message.
        """