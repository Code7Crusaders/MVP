from dto.support_message_dto import SupportMessageDTO
from models.support_message_model import SupportMessageModel
from usecases.save_support_message_useCase import SaveSupportMessageUseCase

class SaveSupportMessageController:
    """
    Controller for saving a support message to the database.
    """

    def __init__(self, save_support_message_usecase: SaveSupportMessageUseCase):
        self.save_support_message_usecase = save_support_message_usecase

    def save_support_message(self, message_dto: SupportMessageDTO):
        """
        Save a support message to the database.

        Args:
            message (SupportMessageDTO): The data transfer object containing support message details.
        Returns:
            int: The ID of the saved support message.        
        """
        try:
        
            message_model = SupportMessageModel(
                id=message_dto.get_id(),
                user_id=message_dto.get_user_id(),
                description=message_dto.get_description(),
                status=message_dto.get_status(),
                subject=message_dto.get_subject(),
                created_at=message_dto.get_created_at()
            )

            return self.save_support_message_usecase.save_support_message(message_model)
        
        except Exception as e:
            raise e
