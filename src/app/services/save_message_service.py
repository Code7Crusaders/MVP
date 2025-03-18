from app.usecases.save_message_useCase import SaveMessageUseCase
from app.ports.save_message_port import SaveMessagePort
from app.models.message_model import MessageModel

class SaveMessageService(SaveMessageUseCase):
    """
    Service class to save conversation titles.
    """
    def __init__(self, save_message_port: SaveMessagePort):
        self.save_message_port = save_message_port
    
    def save_message(self, message: MessageModel):

        """
        Save a message in a conversation.
        """
        self.save_message_port.save_message(MessageModel)
