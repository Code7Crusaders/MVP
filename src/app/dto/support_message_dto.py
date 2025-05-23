from datetime import datetime

class SupportMessageDTO:
    def __init__(self, id: int = None, user_id: int = None, user_email: str = None, description: str = None, status: bool = None, subject: str = None, created_at: datetime = None):
        self.id = id
        self.user_id = user_id
        self.user_email = user_email
        self.description = description
        self.status = status
        self.subject = subject
        self.created_at = created_at 

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id
    
    def get_user_email(self):
        return self.user_email

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_subject(self):
        return self.subject

    def get_created_at(self):
        return self.created_at
