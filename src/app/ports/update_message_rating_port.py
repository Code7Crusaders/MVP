from abc import ABC, abstractmethod
from models.message_model import MessageModel

class UpdateMessageRatingPort(ABC):
    """
    UpdateMessageRatingPort is an interface for updating the rating of a message.
    """
    @abstractmethod
    def update_message_rating(self, message: MessageModel) -> bool:
            """
            Update the rating of a message.
            Args:
                message (MessageModel): The message containing the ID and the new rating value.
            Returns:
                bool: True if the rating was successfully updated, False otherwise.
            """