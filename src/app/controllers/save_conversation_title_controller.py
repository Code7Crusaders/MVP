from usecases.save_conversation_title_useCase import SaveConversationTitleUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

class SaveConversationTitleController:

    def __init__(self, save_conversation_title_usecase: SaveConversationTitleUseCase):
        self.save_conversation_title_usecase = save_conversation_title_usecase

    def save_conversation_title(self, conversation_dto: ConversationDTO) -> int:
        """
        Save a conversation title to the database.
        Args:
            conversation (ConversationDTO): The data transfer object containing conversation details.
        Returns:
            int: The ID of the saved conversation.
        """
        try:
            conversation_model = ConversationModel(
                id=conversation_dto.get_id(),
                title=conversation_dto.get_title()
            )

            return self.save_conversation_title_usecase.save_conversation_title(conversation_model)
        
        except Exception as e:
            raise e