from app.usecases.get_template_useCase import GetTemplateUseCase
from app.ports.get_template_port import GetTemplatePort

class GetTemplateUseCase(GetTemplateUseCase):
    """
    Service class to get templates.
    """
    def __init__(self, get_template_port: GetTemplatePort):
        self.get_template_port = get_template_port
        

    def get_template(self, template_id: int):
        """
        Get the template by its ID.
        """
        return self.get_template_port.get_template(template_id)
