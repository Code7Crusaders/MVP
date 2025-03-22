class QuestionModel:
    """
    Model class to represent a question.
    """
    def __init__(self, user_id: int = None, question: str = None):
        self.user_id = user_id
        self.question = question
        
    def get_user_id(self) -> int:
        return self.user_id
    
    def get_question(self) -> str:
        return self.question