from abc import ABC, abstractmethod
from models.template_model import TemplateModel

class DeleteTemplatePort(ABC):
    """
    DeleteTemplatePort is an abstract base class that defines the interface for deleting templates.
    """

    @abstractmethod
    def delete_template(self, template: TemplateModel) -> bool:
        """
        Delete a template.
        Args:
            template (TemplateModel): The template to delete.
        Returns:
            bool: True if the template was deleted successfully, otherwise False.
        """