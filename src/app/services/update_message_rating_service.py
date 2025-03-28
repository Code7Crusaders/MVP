from ports.update_message_rating_port import UpdateMessageRatingPort
from models.message_model import MessageModel
from usecases.update_message_rating_useCase import UpdateMessageRatingUseCase

class UpdateMessageRatingService(UpdateMessageRatingUseCase):
    """
    Service class to update
    the rating of a message.
    """
    def __init__(self, update_message_rating_port: UpdateMessageRatingPort):
        self.update_message_rating_port = update_message_rating_port

    def update_message_rating(self, message: MessageModel) -> bool:
        """
        Update the rating of a message.
        Args:
            message (MessageModel): The message containing the ID and the new rating value.
        Returns:
            bool: True if the rating was successfully updated, False otherwise.
        """
        try:
            return self.update_message_rating_port.update_message_rating(message)
        except Exception as e:
            raise e
