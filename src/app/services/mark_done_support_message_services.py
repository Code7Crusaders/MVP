from models.support_message_model import SupportMessageModel
from usecases.mark_done_support_messages_useCase import MarkDoneSupportMessagesUseCase
from ports.mark_done_support_messages_port import MarkDoneSupportMessagesPort

class MarkDoneSupportMessagesService(MarkDoneSupportMessagesUseCase):
    """
    Service class to mark support messages as done.
    """
    def __init__(self, mark_done_support_messages_port: MarkDoneSupportMessagesPort):
        """
        Initializes the service with the use case.
        Args:
            mark_done_support_messages_port (MarkDoneSupportMessagesPort): The use case for marking support messages as done.
        """
        self.mark_done_support_messages_port = mark_done_support_messages_port
        

    def mark_done_support_messages(self, support_message_model: SupportMessageModel)-> int:
        """
        Marks support messages as done.
        Args:
            support_message_model (SupportMessageModel): The model containing the support message data.
        """
        try:
    
            return self.mark_done_support_messages_port.mark_done_support_messages(support_message_model)

        except Exception as e:
            raise e