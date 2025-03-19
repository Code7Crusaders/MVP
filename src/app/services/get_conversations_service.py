from app.usecases.get_conversations_useCase import GetConversationsUseCase
from app.models.conversation_model import ConversationModel
from app.ports.get_conversations_port import GetConversationsPort

class GetConversationsService(GetConversationsUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, get_conversations_port: GetConversationsPort):
        self.get_conversations_port = get_conversations_port
        

    def get_conversations(self) -> list[ConversationModel]:
        """
        Get the answer to a user's question.
        """
        return self.get_conversations_port.get_conversations()
