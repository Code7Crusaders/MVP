from app.dto.message_dto import MessageDTO
from app.usecases.save_support_message_useCase import SaveSupportMessageUseCase

class SaveSupportMessageController:
    """
    Controller for saving a support message to the database.
    """

    def __init__(self, save_support_message_usecase: SaveSupportMessageUseCase):
        self.save_support_message_usecase = save_support_message_usecase

    def save_support_message(self, message: MessageDTO):
        """
        Save a support message to the database.

        Args:
            message (MessageDTO): The data transfer object containing support message details.
        """
        try:
            self.save_support_message_usecase.save_support_message(message)
        except Exception as e:
            raise e
