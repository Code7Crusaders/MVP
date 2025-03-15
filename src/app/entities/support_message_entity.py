from datetime import datetime

class SupportMessageEntity():
    def __init__(self, id: int, user_id: int, description: str, status: bool, subject: str, created_at: datetime = None):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.status = status
        self.subject = subject
        self.created_at = created_at or datetime.now()

    def __repr__(self):
        return f"<SupportMessageEntity(id={self.id}, user_id={self.user_id}, description='{self.description}', status={self.status}, subject='{self.subject}', created_at='{self.created_at}')>"

    def mark_as_resolved(self):
        self.status = True

    def get_summary(self) -> str:
        return f"Subject: {self.subject}, Status: {'Resolved' if self.status else 'Unresolved'}"