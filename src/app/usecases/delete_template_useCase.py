from abc import ABC, abstractmethod
from models.template_model import TemplateModel

class DeleteTemplateUseCase(ABC):

    @abstractmethod
    def delete_template(self, template : TemplateModel)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateModel): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """


