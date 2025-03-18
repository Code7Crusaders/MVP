from app.usecases.save_conversation_title_useCase import SaveConversationTitleUseCase
from app.ports.save_conversation_title_port import SaveConversationTitlePort

class SaveConversationTitleService(SaveConversationTitleUseCase):
    """
    Service class to save conversation titles.
    """
    def __init__(self, save_conversation_title_port: SaveConversationTitlePort):
        self.save_conversation_title_port = save_conversation_title_port
        

    def save_conversation_title(self, conversation_id: int, title: str):
        """
        Save the title of a conversation.
        """
        self.save_conversation_title_port.save_conversation_title(conversation_id, title)
