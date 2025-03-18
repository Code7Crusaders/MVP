from app.models.template_model import TemplateModel
from app.ports.save_template_port import SaveTemplatePort

class SaveTemplateService:
    """
    Service class to save templates.
    """
    def __init__(self, save_template_port: SaveTemplatePort):
        self.save_template_port = save_template_port

    def save_template(self, question: str, answer: str, author: str):
        """
        Save a template.
        """
        self.save_template_port.save_template(question, answer, author)
