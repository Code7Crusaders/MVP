from usecases.get_support_message_useCase import GetSupportMessageUseCase
from ports.get_support_message_port import GetSupportMessagePort
from models.support_message_model import SupportMessageModel

class GetSupportMessageService(GetSupportMessageUseCase):
    """
    Service class to get support messages.
    """
    def __init__(self, get_support_message_port: GetSupportMessagePort):
        self.get_support_message_port = get_support_message_port
        

    def get_support_message(self, message: SupportMessageModel) -> SupportMessageModel:
        """
        Retrieves a support message.
        Args:
            message (SupportMessageModel): The support message model containing the details.
        Returns:
            SupportMessageModel: The retrieved support message.
        """
        try:
            return self.get_support_message_port.get_support_message(message)
        except Exception as e:
            raise e
