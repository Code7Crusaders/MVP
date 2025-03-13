class AnswerDTO:
    def __init__(self, answer: str):
        self.answer = answer

    def get_user(self):
        return self.user
    
    def get_answer(self):
        return self.answer
    
    
