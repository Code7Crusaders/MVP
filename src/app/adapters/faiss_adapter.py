from ports.similarity_search_port import SimilaritySearchPort
from ports.add_chunks_port import AddChunksPort

from repositories.faiss_repository import FaissRepository

from models.question_model import QuestionModel
from models.context_model import ContextModel
from models.file_chunk_model import FileChunkModel

from entities.query_entity import QueryEntity
from entities.file_chunk_entity import FileChunkEntity


class FaissAdapter(SimilaritySearchPort, AddChunksPort):

    def __init__(self, faiss_repository: FaissRepository):
        self.faiss_repository = faiss_repository
        
    def similarity_search(self, question_model: QuestionModel) -> list[ContextModel]:
        """
        Perform a similarity search using the provided question model.

        Args:
            question_model (QuestionModel): The model containing the question to search for.

        Returns:
            list[ContextModel]: A list of context models that are similar to the question.
        """
        if not question_model.get_question().strip():
            raise ValueError("Question cannot be empty")

        try:
            query = QueryEntity(question_model.get_user_id , question_model.get_question())
            result = self.faiss_repository.similarity_search(query)

            context_list = []

            for context in result:
                context_list.append( ContextModel(context.get_content()) )

            return context_list
        
        except Exception as e:
            return str(e)
            
    def load_chunks(self, chunks: list[FileChunkModel]):
        """
        Load chunks into the FAISS repository.

        Args:
            chunks (list[FileChunkModel]): A list of file chunk models to be loaded.

        Raises:
            ValueError: If no chunks are provided.

        Returns:
            str: Result of the loading process or an error message.
        """
        if not chunks:
            raise ValueError("No chunks to load.")

        try:
            chunks_entity = []
            for chunk in chunks:
                chunks_entity.append( FileChunkEntity(chunk.get_chunk_content(), chunk.get_metadata()) )

            result = self.faiss_repository.load_chunks(chunks_entity)

            print(result)
            print("Chunks loaded successfully")

        except Exception as e:
            return str(e)
    

