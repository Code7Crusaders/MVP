from app.ports.get_template_list_port import GetTemplateListPort
from app.models.template_model import TemplateModel

class GetTemplateListService:
    """
    Service class to retrieve a list of templates.
    """
    def __init__(self, get_template_list_port: GetTemplateListPort):
        self.get_template_list_port = get_template_list_port

    def get_template_list(self) -> list[TemplateModel]:
        """
        Retrieve a list of templates.
        """
        return self.get_template_list_port.get_template_list()