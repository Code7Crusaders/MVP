from app.usecases.get_support_message_useCase import GetSupportMessageUseCase
from app.ports.get_support_message_port import GetSupportMessagePort
from app.models.support_message_model import SupportMessageModel

class GetSupportMessageService(GetSupportMessageUseCase):
    """
    Service class to get support messages.
    """
    def __init__(self, get_support_message_port: GetSupportMessagePort):
        self.get_support_message_port = get_support_message_port
        

    def get_support_message(self, message_id: int) -> SupportMessageModel:
        """
        Get the support message by message ID.
        """
        return self.get_support_message_port.get_support_message(message_id)
