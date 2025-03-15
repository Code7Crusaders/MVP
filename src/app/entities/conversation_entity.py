class ConversationEntity:
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def get_title(self) -> str:
        return self.title