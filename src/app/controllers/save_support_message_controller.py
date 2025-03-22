from dto.message_dto import MessageDTO
from models.message_model import MessageModel
from usecases.save_support_message_useCase import SaveSupportMessageUseCase

class SaveSupportMessageController:
    """
    Controller for saving a support message to the database.
    """

    def __init__(self, save_support_message_usecase: SaveSupportMessageUseCase):
        self.save_support_message_usecase = save_support_message_usecase

    def save_support_message(self, message_dto: MessageDTO):
        """
        Save a support message to the database.

        Args:
            message (MessageDTO): The data transfer object containing support message details.
        Returns:
            int: The ID of the saved support message.        
        """
        try:
        
            message_model = MessageModel(
                id=message_dto.get_id(),
                user_id=message_dto.get_user_id(),
                text=message_dto.get_text(),
                conversation_id=message_dto.get_conversation_id(),
                rating=message_dto.get_rating(),
                created_at=message_dto.get_created_at()
            )

            return self.save_support_message_usecase.save_support_message(message_model)
        
        except Exception as e:
            raise e
