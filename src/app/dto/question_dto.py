class QuestionDTO:
    def __init__(self, user:int,  question: str):
        self.user = user
        self.question = question

    def get_user(self):
        return self.user
    
    def get_question(self):
        return self.question
    
    
