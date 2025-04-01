from dto.support_message_dto import SupportMessageDTO
from models.support_message_model import SupportMessageModel
from usecases.mark_done_support_messages_useCase import MarkDoneSupportMessagesUseCase


class MarkDoneSupportMessagesController:
    """
    Controller for retrieving support messages from the database.
    """

    def __init__(self, mark_done_support_messages_useCase: MarkDoneSupportMessagesUseCase):
        self.mark_done_support_messages_useCase = mark_done_support_messages_useCase

    def mark_done_support_messages(self, support_message_dto: SupportMessageDTO)-> int:
        try:

            support_message_model = SupportMessageModel(
                id = support_message_dto.get_id(),
                status= support_message_dto.get_status()
            )

            return self.mark_done_support_messages_useCase.mark_done_support_messages(support_message_model)
        
        except Exception as e:
            raise e
