from usecases.delete_template_useCase import DeleteTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel


class DeleteTemplateController:

    def __init__(self, delete_template_use_case: DeleteTemplateUseCase):
        self.delete_template_use_case = delete_template_use_case

    def delete_template(self, template_dto : TemplateDTO)-> bool:
        """
        Delete a template from db.
        Args:
            template (TemplateDTO): The template to be deleted.

        Returns:
            bool: True if the template was deleted, False otherwise.
        """
        try:
            template_model = TemplateModel(
                id=template_dto.get_id(),
                question=template_dto.get_question(),
                answer=template_dto.get_answer(),
                author_id=template_dto.get_author_id(),
                last_modified=template_dto.get_last_modified()
            )

            return self.delete_template_use_case.delete_template(template_model)
        
        except Exception as e:
            raise e