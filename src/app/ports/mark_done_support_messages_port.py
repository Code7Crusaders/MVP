from abc import ABC, abstractmethod
from models.support_message_model import SupportMessageModel

class MarkDoneSupportMessagesPort(ABC):
    """
    MarkDoneSupportMessagesPort is an abstract base class that defines the interface
    for marking support messages as done.
    """

    @abstractmethod
    def mark_done_support_messages(self, support_message_model: SupportMessageModel)-> int:
        """
        Mark a support message as done.
        Args:
            message (SupportMessageModel): The support message to mark as done.
        """
        