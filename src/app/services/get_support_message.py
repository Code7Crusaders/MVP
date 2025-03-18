from app.usecases.get_support_message_useCase import GetSupportMessageUseCase
from app.ports.get_support_message_port import GetSupportMessagePort

class GetSupportMessageService(GetSupportMessageUseCase):
    """
    Service class to get support messages.
    """
    def __init__(self, get_support_message_port: GetSupportMessagePort):
        self.get_support_message_port = get_support_message_port
        

    def get_support_message(self, conversation_id: int):
        """
        Get the support message of a conversation.
        """
        return self.get_support_message.get_supp(conversation_id)
