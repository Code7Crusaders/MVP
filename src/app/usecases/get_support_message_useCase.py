from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class GetSupportMessageUseCase(ABC):

    @abstractmethod
    def get_support_message(self, message: SupportMessageModel) -> SupportMessageModel:
        """
        Retrieves a support message.
        Args:
            message (SupportMessageModel): The support message model containing the details.
        Returns:
            SupportMessageModel: The retrieved support message.
        """
