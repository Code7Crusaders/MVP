from ports.get_template_list_port import GetTemplateListPort
from models.template_model import TemplateModel
from usecases.get_template_list_useCase import GetTemplateListUseCase

class GetTemplateListService(GetTemplateListUseCase):
    """
    Service class to retrieve a list of templates.
    """
    def __init__(self, get_template_list_port: GetTemplateListPort):
        self.get_template_list_port = get_template_list_port

    def get_template_list(self) -> list[TemplateModel]: 
        """
        Retrieve all templates.
        Returns:
            list[TemplateModel]: A list of TemplateModel objects.
        """
        try:
            return self.get_template_list_port.get_template_list()
        except Exception as e:
            raise e