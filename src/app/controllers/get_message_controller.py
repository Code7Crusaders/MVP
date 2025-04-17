from dto.message_dto import MessageDTO
from usecases.get_message_useCase import GetMessageUseCase
from models.message_model import MessageModel


class GetMessageController:
    """
    Controller for retrieving a message from the database.
    """

    def __init__(self, get_message_usecase: GetMessageUseCase):
        
        self.get_message_usecase = get_message_usecase

    def get_message(self, message_dto: MessageDTO) -> MessageDTO:
        """
        Retrieve a message by its ID.
        Args:
            message_dto (MessageDTO): The message DTO containing the ID to retrieve.
        Returns:
            MessageDTO: The retrieved message DTO.
        """
        try:

            message_model = MessageModel(
                id=message_dto.get_id(),
                text=message_dto.get_text(),
                is_bot=message_dto.get_is_bot(),
                conversation_id=message_dto.get_conversation_id(),
                rating=message_dto.get_rating(),
                created_at=message_dto.get_created_at()
            )

            message_result = self.get_message_usecase.get_message(message_model)
            
            if not message_result:
                return None

            return MessageDTO(
                id=message_result.get_id(),
                text=message_result.get_text(),
                is_bot=message_dto.get_is_bot(),
                conversation_id=message_result.get_conversation_id(),
                rating=message_result.get_rating(),
                created_at=message_result.get_created_at()
            )
        
        except Exception as e:
            raise e
