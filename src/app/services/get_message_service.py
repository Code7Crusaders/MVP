from usecases.get_message_useCase import GetMessageUseCase
from ports.get_message_port import GetMessagePort
from models.message_model import MessageModel

class GetMessageService(GetMessageUseCase):
    """
    Service class to get messages.
    """
    def __init__(self, get_message_port: GetMessagePort):
        self.get_message_port = get_message_port
        

    def get_message(self, message: MessageModel) -> MessageModel:
        """
        Retrieve a message by its ID.
        Args:
            message (MessageModel): The message object containing the ID to retrieve.
        Returns:
            MessageModel: The retrieved message.
        """
        try:

            return self.get_message_port.get_message(message)

        except Exception as e:
            raise e