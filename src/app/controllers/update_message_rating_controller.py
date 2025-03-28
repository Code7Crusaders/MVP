from dto.message_dto import MessageDTO
from models.message_model import MessageModel
from usecases.update_message_rating_useCase import UpdateMessageRatingUseCase

class UpdateMessageRatingController:
    """
    Controller for updating the rating of a message.
    """

    def __init__(self, update_message_rating_usecase: UpdateMessageRatingUseCase):
        self.update_message_rating_usecase = update_message_rating_usecase

    def update_message_rating(self, message_dto: MessageDTO) -> bool:
        """
        Updates the rating of a message in the database.

        Args:
            message_dto (MessageDTO): The data transfer object containing message details.
        Returns:
            bool: True if the rating was successfully updated, False otherwise.
        """
        try:
            message_model = MessageModel(
                id=message_dto.get_id(),
                rating=message_dto.get_rating(),
            )

            return self.update_message_rating_usecase.update_message_rating(message_model)
        
        except Exception as e:
            raise e
