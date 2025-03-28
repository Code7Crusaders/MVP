from usecases.delete_conversation_useCase import DeleteConversationUseCase
from dto.conversation_dto import ConversationDTO
from models.conversation_model import ConversationModel 


class DeleteConversationController:

    def __init__(self, delete_conversation_use_case: DeleteConversationUseCase):
        self.delete_conversation_use_case = delete_conversation_use_case

    def delete_conversation(self, conversation_dto : ConversationDTO)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateDTO): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """
        try:
            conversation_model = ConversationDTO(
                id=conversation_dto.get_id(),
                title=conversation_dto.get_title(),
                user_id=conversation_dto.get_user_id()
            )

            return self.delete_conversation_use_case.delete_conversation(conversation_model)
        
        except Exception as e:
            raise e