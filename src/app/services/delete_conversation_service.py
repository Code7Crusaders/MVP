from usecases.delete_conversation_useCase import DeleteConversationUseCase
from ports.delete_conversation_port import DeleteConversationPort
from models.conversation_model import ConversationModel

class DeleteConversationService(DeleteConversationUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, delete_conversation_port: DeleteConversationPort):
        self.delete_conversation_port = delete_conversation_port
        

    def delete_conversation(self, conversation : ConversationModel)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateModel): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """
        try:
            return self.delete_conversation_port.delete_conversation_title(conversation)
        except Exception as e:
            raise e
        

