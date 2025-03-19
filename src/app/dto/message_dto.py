from datetime import datetime

class MessageDTO:
    def __init__(self, text: str, conversation_id: int, rating: bool, created_at: datetime, id: int = None, user_id: int = None):
        self.id = id
        self.text = text
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.rating = rating
        self.created_at = created_at 

    def get_id(self):
        return self.id

    def get_text(self):
        return self.text

    def get_user_id(self):
        return self.user_id

    def get_conversation_id(self):
        return self.conversation_id

    def get_rating(self):
        return self.rating

    def get_created_at(self):
        return self.created_at

