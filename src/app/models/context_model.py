
class ContextModel:
    """
    Model class for a File context.
    """
    def __init__(self, content: str):
        self.content = content

    def get_content(self) -> str:
        return self.content