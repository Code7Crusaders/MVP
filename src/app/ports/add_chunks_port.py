from abc import ABC, abstractmethod
from models.file_chunk_model import FileChunkModel

class AddChunksPort(ABC):

    @abstractmethod
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