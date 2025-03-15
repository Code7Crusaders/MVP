class TemplateEntity():
    def __init__(self, id: int, question: str, answer: str, author: str, last_modified: str):
        self.id = id
        self.question = question
        self.answer = answer
        self.author = author
        self.last_modified = last_modified

    def get_question(self) -> str:
        return self.question

    def get_answer(self) -> str:
        return self.answer

    def get_author(self) -> str:
        return self.author

    def get_id(self) -> int:
        return self.id

    def get_last_modified(self) -> str:
        return self.last_modified