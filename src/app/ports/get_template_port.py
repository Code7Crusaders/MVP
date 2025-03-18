from abc import ABC, abstractmethod
from app.models.template_model import TemplateModel

class GetTemplatePort(ABC):
    """
    GetTemplatePort is an abstract base class that defines the interface for getting templates.
    """

    @abstractmethod
    def get_template(self, template_id: int) -> TemplateModel:
        """
        Get a template by its ID.
        Args:
            template_id (int): The ID of the template.
        Returns:
            TemplateModel: The template model.
        """
        pass