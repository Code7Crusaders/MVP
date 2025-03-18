from app.ports.save_support_message_port import SaveSupportMessagePort
from app.models.support_message_model import SupportMessageModel

class SaveSupportMessageService:
    """
    Service class to save a support message.
    """
    def __init__(self, save_support_message_port: SaveSupportMessagePort):
        self.save_support_message_port = save_support_message_port
    
    def save_support_message(self, user_id: int, description: str, status: str, subject: str) -> SupportMessageModel:
        """
        Save a support message with the given details.
        """
        return self.save_support_message_port.save_support_message(user_id, description, status, subject)
