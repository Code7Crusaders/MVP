from abc import ABC, abstractmethod

from models.file_chunk_model import FileChunkModel
from models.file_model import FileModel

class SplitFilePort(ABC):

    @abstractmethod
    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        """
        Splits the given file into chunks.

        Args:
            file (FileModel): The file model containing the filename and file content.

        Returns:
            list[FileChunkModel]: A list of file chunk models containing the chunk content and metadata.
        """