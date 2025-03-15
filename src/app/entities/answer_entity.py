class AnswerEntity:

    def __init__(self, answer: str):
        self.answer = answer

    def get_answer(self) -> str:
        return self.answer