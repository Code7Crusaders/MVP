class ConversationEntity:
    def __init__(self, title: str, id: int = None):
        self.id = id
        self.title = title

    def get_title(self) -> str:
        return self.title
    
    def get_id(self) -> int:
        return self.id