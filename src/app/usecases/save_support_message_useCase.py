from app.usecases.save_support_message_useCase import SaveSupportMessageUseCase
from app.ports.save_support_message_port import SaveSupportMessagePort

class SaveSupportMessageUseCase(SaveSupportMessageUseCase):
    """
    Service class to handle support messages
    """
    def __init__(self, save_support_message_port: SaveSupportMessagePort):
        self.save_support_message_port = save_support_message_port

    def save_support_message(self, user_id: int, description: str, status: str, subject: str):
        """
        Save a support message with the given details.
        """
        return self.save_support_message_port.save_support_message(user_id, description, status, subject)
