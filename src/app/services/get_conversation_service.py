from app.usecases.get_conversation_useCase import GetConversationUseCase
from app.models.conversation_model import ConversationModel
from app.ports.get_conversation_port import GetConversationPort

class GetConversationService(GetConversationUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, get_conversation_port: GetConversationPort):
        self.get_conversation_port = get_conversation_port
        

    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        Get the answer to a user's question.
        """
        return self.get_conversation_port.get_conversation(conversation.get_id())
