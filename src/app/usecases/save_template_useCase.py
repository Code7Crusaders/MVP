from abc import ABC, abstractmethod
from models.template_model import TemplateModel

class SaveTemplateUseCase(ABC):
    """
    Service class to handle templates
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