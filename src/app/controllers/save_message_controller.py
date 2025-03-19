from app.dto.message_dto import MessageDTO
from app.usecases.save_message_useCase import SaveMessageUseCase

class SaveMessageController:
    """
    Controller for saving a message to the database.
    """

    def __init__(self, save_message_usecase: SaveMessageUseCase):
        self.save_message_usecase = save_message_usecase

    def save_message(self, message: MessageDTO):
        """
        Save a message to the database.

        Args:
            message (MessageDTO): The data transfer object containing message details.
        """
        try:
            self.save_message_usecase.save_message(message)
        except Exception as e:
            raise e
