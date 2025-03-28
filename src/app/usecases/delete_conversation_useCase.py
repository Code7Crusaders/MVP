from abc import ABC, abstractmethod
from models.conversation_model import ConversationModel

class DeleteConversationUseCase(ABC):

    @abstractmethod
    def delete_conversation(self, conversation : ConversationModel)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateModel): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """


