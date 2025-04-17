from abc import ABC, abstractmethod
from models.template_model import TemplateModel

class GetTemplateUseCase(ABC):
        
    @abstractmethod
    def get_template(self, template: TemplateModel) -> TemplateModel:
        """
        Retrieve a template by its details.
        Args:
            template (TemplateModel): The template details to retrieve.
        Returns:
            TemplateModel: The retrieved template.
        """
