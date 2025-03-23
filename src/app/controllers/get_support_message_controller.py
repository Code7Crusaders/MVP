from dto.support_message_dto import SupportMessageDTO
from usecases.get_support_message_useCase import GetSupportMessageUseCase
from models.support_message_model import SupportMessageModel


class GetSupportMessageController:
    """
    Controller for retrieving a support message from the database.
    """

    def __init__(self, get_support_message_usecase: GetSupportMessageUseCase):
        self.get_support_message_usecase = get_support_message_usecase

    def get_support_message(self, support_message_dto: SupportMessageDTO) -> SupportMessageDTO:
        """
        Retrieve a support message from the database.
        
        Args:
            support_message_dto (SupportMessageDTO): The data transfer object containing support message details.

        Returns:
            SupportMessageDTO: The data transfer object containing support message details.
        """
        try:
            support_message_model = SupportMessageModel(
                id=support_message_dto.get_id(),
                user_id=support_message_dto.get_user_id(),
                description=support_message_dto.get_description(),
                status=support_message_dto.get_status(),
                subject=support_message_dto.get_subject(),
                created_at=support_message_dto.get_created_at()
            )

            result_model = self.get_support_message_usecase.get_support_message(support_message_model)
            
            if not result_model:
                return None

            return SupportMessageDTO(
                id=result_model.get_id(),
                user_id=result_model.get_user_id(),
                description=result_model.get_description(), 
                status=result_model.get_status(),
                subject=result_model.get_subject(),
                created_at=result_model.get_created_at()
            )
        
        except Exception as e:
            raise e
