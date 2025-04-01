from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class MarkDoneSupportMessagesUseCase(ABC):

    @abstractmethod
    def mark_done_support_messages(self, support_message_model: SupportMessageModel):
        """
        Marks support messages as done.
        Args:
            support_message_model (SupportMessageModel): The MODEL containing the support message data.
        """
        
        
