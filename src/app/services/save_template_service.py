from models.template_model import TemplateModel
from ports.save_template_port import SaveTemplatePort
from usecases.save_template_useCase import SaveTemplateUseCase

class SaveTemplateService(SaveTemplateUseCase):
    """
    Service class to save templates.
    """
    def __init__(self, save_template_port: SaveTemplatePort):
        self.save_template_port = save_template_port

    def save_template(self, template: TemplateModel) -> int:
        """
        Save a template.
        Args:
            template (TemplateModel): The template to save.
        Returns:
            int: The ID of the saved template.
        """
        try:
            return self.save_template_port.save_template(template)
        except Exception as e:
            raise e
