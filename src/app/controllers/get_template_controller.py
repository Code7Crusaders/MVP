from usecases.get_template_useCase import GetTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

class GetTemplateController:

    def __init__(self, get_template_use_case: GetTemplateUseCase):
        self.get_template_use_case = get_template_use_case

    def get_template(self, template_dto: TemplateDTO) -> TemplateDTO:
        """
        get the template from db using id to get it.
        Args:
            template (TemplateDTO): The template to be retrieved.
        Returns:
            TemplateDTO: The template retrieved from db.
        """
        try:
            template_model = TemplateModel(
                id=template_dto.get_id(),
                question=template_dto.get_question(),
                answer=template_dto.get_answer(),
                author_id=template_dto.get_author_id(),
                last_modified=template_dto.get_last_modified()
            )

            template_result = self.get_template_use_case.get_template(template_model)

            return TemplateDTO(
                id=template_result.get_id(),
                question=template_result.get_question(),
                answer=template_result.get_answer(),
                author_id=template_result.get_author_id(),
                last_modified=template_result.get_last_modified()
            )

        except Exception as e:
            raise e