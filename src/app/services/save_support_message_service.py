from ports.save_support_message_port import SaveSupportMessagePort
from models.support_message_model import SupportMessageModel
from usecases.save_support_message_useCase import SaveSupportMessageUseCase

class SaveSupportMessageService(SaveSupportMessageUseCase):
    """
    Service class to save a support message.
    """
    def __init__(self, save_support_message_port: SaveSupportMessagePort):
        self.save_support_message_port = save_support_message_port
    
    def save_support_message(self, support_message: SupportMessageModel)-> int:
        """
        Save a support message.
        Args:
            support_message (SupportMessageModel): The support message to save.
        Returns:
            int: The ID of the saved support message.
        """
        try:
            return self.save_support_message_port.save_support_message(support_message)
        except Exception as e:
            raise e
