from dto.message_dto import MessageDTO
from usecases.get_messages_by_conversation_useCase import GetMessagesByConversationUseCase
from typing import List


class GetMessagesByConversationController:
    """
    Controller for retrieving messages by conversation from the database.
    """

    def __init__(self, get_messages_by_conversation_usecase: GetMessagesByConversationUseCase):
        self.get_messages_by_conversation_usecase = get_messages_by_conversation_usecase

    def get_messages_by_conversation(self, conversation_dto: MessageDTO) -> List[MessageDTO]:
        """
        Retrieve messages from the database by conversation DTO.
        """
        try:
            # Validazione sull'input
            if not conversation_dto.get_conversation_id():
                raise ValueError("Invalid conversation ID")

            conversation_model = MessageDTO(
                id=conversation_dto.get_id(),
                text=conversation_dto.get_text(),
                is_bot=conversation_dto.get_is_bot(),
                conversation_id=conversation_dto.get_conversation_id(),
                rating=conversation_dto.get_rating(),
                created_at=conversation_dto.get_created_at()
            ) 

            result_models = self.get_messages_by_conversation_usecase.get_messages_by_conversation(conversation_model)

            return [
                MessageDTO(
                    id=model.get_id(),
                    text=model.get_text(),
                    is_bot=model.get_is_bot(),
                    conversation_id=model.get_conversation_id(),
                    rating=model.get_rating(),
                    created_at=model.get_created_at()
                )
                for model in result_models
            ]
        except Exception as e:
            raise e
