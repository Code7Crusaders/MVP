from usecases.get_conversations_useCase import GetConversationsUseCase
from models.conversation_model import ConversationModel
from ports.get_conversations_port import GetConversationsPort

class GetConversationsService(GetConversationsUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, get_conversations_port: GetConversationsPort):
        self.get_conversations_port = get_conversations_port
        

    def get_conversations(self, user_id : int) -> list[ConversationModel]:
        """
        Get all conversations.
        Returns:
            List[ConversationModel]: A list of conversation models.
        """
        try:
            
            return self.get_conversations_port.get_conversations(user_id)

        except Exception as e:
            raise e