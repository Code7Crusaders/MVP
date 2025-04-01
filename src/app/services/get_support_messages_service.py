from ports.get_support_messages_port import GetSupportMessagesPort
from models.support_message_model import SupportMessageModel
from usecases.get_support_messages_useCase import GetSupportMessagesUseCase

class GetSupportMessagesService(GetSupportMessagesUseCase):
    """
    Service class to retrieve a support message by its ID.
    """
    def __init__(self, get_support_messages_port: GetSupportMessagesPort):
        self.get_support_messages_port = get_support_messages_port
    
    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Retrieves all support messages, ordered by status and creation date.
        Returns:
            list[SupportMessageModel]: A list of support messages.
        """
        try:
            messages = self.get_support_messages_port.get_support_messages()
            
            sorted_messages = sorted(
                messages,
                key=lambda msg: (msg.status, -msg.created_at.timestamp())
            )
            
            return sorted_messages

        except Exception as e:
            raise e
