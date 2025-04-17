from usecases.save_message_useCase import SaveMessageUseCase
from ports.save_message_port import SaveMessagePort
from models.message_model import MessageModel

class SaveMessageService(SaveMessageUseCase):
    """
    Service class to save conversation titles.
    """
    def __init__(self, save_message_port: SaveMessagePort):
        self.save_message_port = save_message_port
    
    def save_message(self, message: MessageModel)-> int:
        """
        Save a message.
        Args:
            message (MessageModel): The message model.
        Returns:
            int: The ID of the saved message.
        """
        try:
            return self.save_message_port.save_message(message)
        except Exception as e:
            raise e
