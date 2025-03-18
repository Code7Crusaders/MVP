from abc import ABC, abstractmethod

from models.file_chunk_model import FileChunkModel
from models.file_model import FileModel

class SplitFilePort(ABC):

    @abstractmethod
    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        pass