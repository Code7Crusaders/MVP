from app.ports.get_support_messages_port import GetSupportMessagesPort
from app.models.support_message_model import SupportMessageModel

class GetSupportMessagesService:
    """
    Service class to retrieve a support message by its ID.
    """
    def __init__(self, get_support_messages_port: GetSupportMessagesPort):
        self.get_support_messages_port = get_support_messages_port
    
    def get_support_messages(self) -> list[SupportMessageModel]:
        """
        Retrieve all support messages.
        """
        return self.get_support_messages_port.get_support_messages()
