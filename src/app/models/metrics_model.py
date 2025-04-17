class MetricsModel:

    def __init__(self, total_likes, total_dislikes, total_messages, positive_rating):
        self.total_likes = total_likes
        self.total_dislikes = total_dislikes
        self.total_messages = total_messages
        self.positive_rating = positive_rating

    def get_total_likes(self):
        return self.total_likes
    
    def get_total_dislikes(self):
        return self.total_dislikes
    
    def get_total_messages(self):
        return self.total_messages
    
    def get_positive_rating(self):
        return self.positive_rating
    
    