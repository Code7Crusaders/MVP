from ports.get_template_port import GetTemplatePort
from models.template_model import TemplateModel
from usecases.get_template_useCase import GetTemplateUseCase

class GetTemplateService(GetTemplateUseCase):
    """
    Service class to retrieve
    a template by its ID.
    """
    def __init__(self, get_template_port: GetTemplatePort):
        self.get_template_port = get_template_port

    def get_template(self, template: TemplateModel) -> TemplateModel:
        """
        Retrieve a template by its details.
        Args:
            template (TemplateModel): The template details to retrieve.
        Returns:
            TemplateModel: The retrieved template.
        """
        try:
            return self.get_template_port.get_template(template)
        except Exception as e:
            raise e
