from app.usecases.get_conversation_useCase import GetConversationUseCase
from app.models.conversation_model import ConversationModel
from app.ports.get_conversation_port import GetConversationPort

class GetConversationService(GetConversationUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, get_conversation: GetConversationPort):
        self.get_conversation = get_conversation
        

    def get_conversation_answer(self, conversation_id: int) -> ConversationModel:
        """
        Get the answer to a user's question.
        """
        return self.conversation_port.get_conversation(conversation_id)
