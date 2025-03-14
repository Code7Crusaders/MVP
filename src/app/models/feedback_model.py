class FeedbackModel:
    def __init__(self, id, user_id, description, status, subject, created_at):
        self.id = id
        self.user_id = user_id
        self.description = description
        self.status = status
        self.subject = subject
        self.created_at = created_at

    # ...existing code...
