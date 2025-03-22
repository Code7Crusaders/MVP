from usecases.save_template_useCase import SaveTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

class SaveTemplateController:

    def __init__(self, save_template_usecase: SaveTemplateUseCase):
        self.save_template_usecase = save_template_usecase

    def save_template(self, template_dto: TemplateDTO) -> int:
        """
        Save a template to the database.
        Args:
            template (TemplateDTO): The data transfer object containing template details.
        Returns:
            int: The ID of the saved template.
        """
        try:
            template_model = TemplateModel(
                id=template_dto.get_id(),
                question=template_dto.get_question(),
                answer=template_dto.get_answer(),
                author_id=template_dto.get_author_id(),
                last_modified=template_dto.get_last_modified()
            )

            return self.save_template_usecase.save_template(template_model)
        
        except Exception as e:
            raise e