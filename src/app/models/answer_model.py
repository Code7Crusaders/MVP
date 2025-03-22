class AnswerModel:

    def __init__(self, answer: str = None):
        self.answer = answer

    def get_answer(self) -> str:
        return self.answer