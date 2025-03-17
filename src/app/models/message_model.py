from datetime import datetime

class MessageModel:
    def __init__(self, id: int, text: str, user_id: int, conversation_id: int, rating: bool, is_bot: bool = False, created_at: datetime = None):
        self.id = id
        self.text = text
        self.user_id = user_id
        self.conversation_id = conversation_id
        self.rating = rating
        self.is_bot = is_bot
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"<Message(id={self.id}, text='{self.text}', created_at='{self.created_at}', user_id={self.user_id}, conversation_id={self.conversation_id}, rating={self.rating}, is_bot={self.is_bot})>"

    def mark_as_bot(self):
        self.is_bot = True

    def get_summary(self) -> str:
        return f"Text: {self.text}, User ID: {self.user_id}, Conversation ID: {self.conversation_id}, Rating: {self.rating}, Is Bot: {self.is_bot}"