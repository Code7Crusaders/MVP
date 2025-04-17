from usecases.get_conversation_useCase import GetConversationUseCase
from models.conversation_model import ConversationModel
from ports.get_conversation_port import GetConversationPort

class GetConversationService(GetConversationUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, get_conversation_port: GetConversationPort):
        self.get_conversation_port = get_conversation_port
        

    def get_conversation(self, conversation: ConversationModel) -> ConversationModel:
        """
        get the conversation title from db using id to get it.
        Args:
            conversation (ConversationModel): The conversation to be retrieved.
        Returns:
            ConversationModel: The conversation retrieved from db.
        """
        try: 
        
            return self.get_conversation_port.get_conversation(conversation)
        
        except Exception as e:
            raise e
        
