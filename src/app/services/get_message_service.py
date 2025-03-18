from app.usecases.get_message_useCase import GetMessageUseCase
from app.ports.get_message_port import GetMessagePort
from app.models.message_model import MessageModel

class GetMessageService(GetMessageUseCase):
    """
    Service class to get messages.
    """
    def __init__(self, get_message_port: GetMessagePort):
        self.get_message_port = get_message_port
        

    def get_message(self, message_id: int) -> MessageModel:
        """
        Retrieve a message by its ID.
        """
        return self.get_message_port.get_message(message_id)
