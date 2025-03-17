from abc import ABC, abstractmethod
from models.file_chunk_model import FileChunkModel

class AddChunksPort(ABC):

    @abstractmethod
    def load_chunks(self, chunks: list[FileChunkModel]):
        pass