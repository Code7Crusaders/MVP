from abc import ABC, abstractmethod
import app.models.template_model as TemplateModel

class SaveTemplatePort(ABC):
    """
    SaveTemplatePort is an abstract base class that defines the interface for saving templates.
    """

    @abstractmethod
    def save_template(self, template: TemplateModel) -> int:
        """
        Save a template.
        Args:
            template (TemplateModel): The template to save.
        Returns:
            int: The ID of the saved template.
        """
        