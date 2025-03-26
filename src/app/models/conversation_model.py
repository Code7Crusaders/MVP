class ConversationModel:
    def __init__(self, title: str = None, id: int = None, user_id: int = None):
        self.id = id
        self.title = title
        self.user_id = user_id


    def get_title(self) -> str:
        return self.title
    
    def get_id(self) -> int:
        return self.id
    
    def get_user_id(self) -> int:
        return self.user_id