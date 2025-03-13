

class QueryEntity:
    def __init__(self, user_id: int, query: str):
        self.user_id = user_id
        self.query = query

    def get_user_id(self) -> int:
        return self.user_id
    
    def get_query(self) -> str:
        return self.query
    
    