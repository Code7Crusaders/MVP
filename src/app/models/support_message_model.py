from datetime import datetime

class SupportMessageModel:
    def __init__(self, user_id: int, description: str, status: bool, subject: str, created_at: datetime, id: int = None):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.status = status
        self.subject = subject
        self.created_at = created_at 

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_subject(self):
        return self.subject

    def get_created_at(self):
        return self.created_at
