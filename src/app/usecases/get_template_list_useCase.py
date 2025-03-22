from abc import ABC, abstractmethod
from models.template_model import TemplateModel


class GetTemplateListUseCase(ABC):

    @abstractmethod
    def get_template_list(self) -> list[TemplateModel]: 
        """
        Retrieve all templates.
        Returns:
            list[TemplateModel]: A list of TemplateModel objects.
        """