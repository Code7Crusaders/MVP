from datetime import datetime

class MessageDTO:
    def __init__(self, id: int, text: str, user_id: int, conversation_id: int, rating: bool, is_bot: bool = False, created_at: datetime = None):
        self.id = id
        self.text = text
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.rating = rating
        self.is_bot = is_bot
        self.created_at = created_at or datetime.now()

