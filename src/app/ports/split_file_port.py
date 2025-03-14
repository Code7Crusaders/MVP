from abc import ABC, abstractmethod

from app.models.file_chunk_model import FileChunkModel
from app.models.file_model import FileModel

class SplitFilePort(ABC):

    @abstractmethod
    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        pass