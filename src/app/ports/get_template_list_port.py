from abc import ABC, abstractmethod
from app.models.template_model import TemplateModel

class GetTemplateListPort(ABC):
    """
    GetTemplateListPort is an abstract base class that defines the interface for retrieving a list of templates.
    """

    @abstractmethod
    def get_template_list(self) -> list[TemplateModel]:
        """
        Retrieve a list of templates.
        Returns:
            list[TemplateModel]: A list of template models.
        """
