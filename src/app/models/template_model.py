class TemplateModel:

    def __init__(self, question: str, answer: str, author: str):
        self.question = question
        self.answer = answer
        self.author = author

    def get_question(self) -> str:
        return self.question

    def get_answer(self) -> str:
        return self.answer

    def get_author(self) -> str:
        return self.author