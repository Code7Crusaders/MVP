from app.ports.get_messages_by_conversation import GetMessagesByConversationPort
from app.models.message_model import MessageModel

class GetMessagesByConversationService:
    """
    Service class to retrieve messages by conversation ID.
    """
    def __init__(self, get_messages_by_conversation_port: GetMessagesByConversationPort):
        self.get_messages_by_conversation_port = get_messages_by_conversation_port
    
    def get_messages_by_conversation(self, conversation_id: int) -> list[MessageModel]:
        """
        Retrieve messages in a conversation by its ID.
        """
        return self.get_messages_by_conversation_port.get_messages_by_conversation(conversation_id)
