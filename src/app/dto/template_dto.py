from datetime import datetime

class TemplateDTO:
    def __init__(self, question: str = None, answer: str = None, author_id: int = None, last_modified: datetime = None, id: int = None):
        self.id = id
        self.question = question
        self.answer = answer
        self.author_id = author_id
        self.last_modified = last_modified

    def get_id(self) -> int:
        return self.id

    def get_question(self) -> str:
        return self.question

    def get_answer(self) -> str:
        return self.answer

    def get_author_id(self) -> int:
        return self.author_id

    def get_last_modified(self) -> datetime:
        return self.last_modified