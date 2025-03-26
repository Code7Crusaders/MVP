from usecases.get_conversation_useCase import GetConversationUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel

class GetConversationController:

    def __init__(self, get_conversation_use_case: GetConversationUseCase):
        self.get_conversation_use_case = get_conversation_use_case

    def get_conversation(self, conversation_dto: ConversationDTO) -> ConversationDTO:
        """
        get the conversation title from db using id to get it.
        Args:
            conversation (ConversationDTO): The conversation to be retrieved.
        Returns:
            ConversationDTO: The conversation retrieved from db.
        """
        try:
            conversation_model = ConversationModel(
                id=conversation_dto.get_id(),
                title=conversation_dto.get_title(),
                user_id=conversation_dto.get_user_id()
            )

            conversation_result = self.get_conversation_use_case.get_conversation(conversation_model)

            return ConversationDTO(
                id=conversation_result.get_id(),
                title=conversation_result.get_title(),
                user_id=conversation_result.get_user_id()
            )

        except Exception as e:
            raise e