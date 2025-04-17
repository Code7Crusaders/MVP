from dto.message_dto import MessageDTO
from models.message_model import MessageModel
from usecases.save_message_useCase import SaveMessageUseCase

class SaveMessageController:
    """
    Controller for saving a message to the database.
    """

    def __init__(self, save_message_usecase: SaveMessageUseCase):
        self.save_message_usecase = save_message_usecase

    def save_message(self, message_dto: MessageDTO):
        """
        Save a message to the database.

        Args:
            message (MessageDTO): The data transfer object containing message details.
        Returns:
            int: The ID of the saved message.
        """

        try:
            message_model = MessageModel(
                id=message_dto.get_id(),
                text=message_dto.get_text(),
                is_bot=message_dto.get_is_bot(),
                conversation_id=message_dto.get_conversation_id(),
                rating=message_dto.get_rating(),
                created_at=message_dto.get_created_at()
            )

            return self.save_message_usecase.save_message(message_model)
        
        except Exception as e:
            raise e
