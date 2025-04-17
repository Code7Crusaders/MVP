from models.question_model import QuestionModel
from models.context_model import ContextModel 

from ports.similarity_search_port import SimilaritySearchPort

class SimilaritySearchService:
    def __init__(self, similarity_search_port: SimilaritySearchPort):
        self.similarity_search_port = similarity_search_port

    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:
        """
        Performs a similarity search based on the user input and returns a list of relevant documents.
        Args:
            question_model (QuestionModel): The input question for which similar documents are to be searched.
        Returns:
            list[ContextModel]: A list of documents that are relevant to the user input.
        Raises:
            Exception: If an error occurs during the similarity search.
        """
        try: 
            return self.similarity_search_port.similarity_search(question_model)
        except Exception as e:
            raise Exception(f"An error occurred during the similarity search: {e}") from e