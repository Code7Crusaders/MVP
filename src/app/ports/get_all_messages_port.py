from abc import ABC, abstractmethod
from models.message_model import MessageModel

class GetAllMessagesPort(ABC):
    """
    Abstract interface for fetching dashboard metrics data.
    """

    @abstractmethod
    def fetch_messages(self) -> list[MessageModel]:
        """
        Fetch the dashboard metrics data.
        Returns:
            list[MessageModel]: A list of MessageModel objects containing the messages data.
        """
        
        