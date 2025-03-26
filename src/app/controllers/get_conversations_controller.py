from usecases.get_conversations_useCase import GetConversationsUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

class GetConversationsController:

    def __init__(self, get_conversations_use_case: GetConversationsUseCase):
        self.get_conversations_use_case = get_conversations_use_case

    def get_conversations(self, conversation : ConversationDTO) -> list[ConversationDTO]:
        """
        Get all conversations from the database.
        Returns:
            list[ConversationDTO]: A list of conversations retrieved from the database.
        """
        try:

            conversation_model = ConversationModel(
                id=conversation.get_id(),
                title=conversation.get_title(),
                user_id=conversation.get_user_id()
            )
            
            conversations_result = self.get_conversations_use_case.get_conversations(conversation_model)

            return [
                ConversationDTO(
                    id=conversation.get_id(),
                    title=conversation.get_title(),
                    user_id=conversation.get_user_id()
                )
                for conversation in conversations_result
            ]

        except Exception as e:
            raise e