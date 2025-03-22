from usecases.save_conversation_title_useCase import SaveConversationTitleUseCase
from ports.save_conversation_title_port import SaveConversationTitlePort
from models.conversation_model import ConversationModel

class SaveConversationTitleService(SaveConversationTitleUseCase):
    """
    Service class to save conversation titles.
    """
    def __init__(self, save_conversation_title_port: SaveConversationTitlePort):
        self.save_conversation_title_port = save_conversation_title_port
        

    def save_conversation_title(self, conversation: ConversationModel) -> int:
        """
        Save a conversation title by its ID.
        Args:
            conversation (ConversationModel): The conversation model containing the ID and title.
        Returns:
            int: The ID of the updated conversation.
        """
        try:
            return self.save_conversation_title_port.save_conversation_title(conversation)
        except Exception as e:
            raise e

