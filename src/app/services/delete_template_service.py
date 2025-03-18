from app.usecases.delete_template_useCase import DeleteTemplateUseCase
from app.ports.delete_template_port import DeleteTemplatePort

class DeleteTemplateService(DeleteTemplateUseCase):
    """
    Service class to manage chat interactions.
    """
    def __init__(self, delete_template_port: DeleteTemplatePort):
        self.delete_template_port = delete_template_port
        

    def delete_template(self, author: str, question: str, answer: str):
        """
        Get the answer to a user's question.
        """
        return self.delete_template_port.delete_template(author, question, answer)
