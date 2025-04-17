from usecases.delete_template_useCase import DeleteTemplateUseCase
from ports.delete_template_port import DeleteTemplatePort
from models.template_model import TemplateModel

class DeleteTemplateService(DeleteTemplateUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, delete_template_port: DeleteTemplatePort):
        self.delete_template_port = delete_template_port
        

    def delete_template(self, template : TemplateModel)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateModel): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """
        try:
            return self.delete_template_port.delete_template(template)
        except Exception as e:
            raise e
        

