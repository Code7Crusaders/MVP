from ports.get_messages_by_conversation_port import GetMessagesByConversationPort
from models.message_model import MessageModel

from usecases.get_messages_by_conversation_useCase import GetMessagesByConversationUseCase

class GetMessagesByConversationService(GetMessagesByConversationUseCase):
    """
    Service class to retrieve messages by conversation ID.
    """
    def __init__(self, get_messages_by_conversation_port: GetMessagesByConversationPort):
        self.get_messages_by_conversation_port = get_messages_by_conversation_port
    
    def get_messages_by_conversation(self, conversation: MessageModel) -> list[MessageModel]:
        """
        Retrieve messages by conversation.
        Args:
            conversation (MessageModel): The conversation object containing the ID to retrieve messages for.
        Returns:
            list[MessageModel]: A list of retrieved messages, ordered by creation time.
        """
        try:
            messages = self.get_messages_by_conversation_port.get_messages_by_conversation(conversation)
            # Sort messages by the created_at attribute
            return sorted(messages, key=lambda message: message.get_created_at() or "")
        except Exception as e:
            raise e
