from abc import ABC, abstractmethod
from app.models.template_model import TemplateModel

class GetTemplatePort(ABC):
    """
    GetTemplatePort is an abstract base class that defines the interface for getting templates.
    """

    @abstractmethod
    def get_template(self, template: TemplateModel) -> TemplateModel:
        """
        Retrieve a template by its details.
        Args:
            template (TemplateModel): The template details to retrieve.
        Returns:
            TemplateModel: The retrieved template.
        """