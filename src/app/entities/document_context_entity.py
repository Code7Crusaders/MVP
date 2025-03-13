class DocumentContextEntity:
    def __init__(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content
        