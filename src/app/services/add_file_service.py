from app.services.split_file_service import SplitFileService
from app.services.add_chunks_service import AddChunksService
from app.models.file_model import FileModel
from app.models.file_chunk_model import FileChunkModel

class AddFileService:
    """
    Service class to manage file addition.
    """
    def __init__(self, split_file_service: SplitFileService, add_chunks_service: AddChunksService):
        self.split_file_service = split_file_service
        self.add_chunks_service = add_chunks_service

    def load_file(self, file: FileModel):
        """
        Load a file and process its chunks.
        """
        try:
            chunks = self.split_file(file)
            self.load_chunks(chunks)
        except Exception as e:
            raise e

    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        """
        Split the file into chunks.
        """
        try:
            return self.split_file_service.split_file(file)
        except Exception as e:
            raise e

    def load_chunks(self, chunks: list[FileChunkModel]):
        """
        Load the file chunks.
        """
        try:
            self.add_chunks_service.load_chunks(chunks)
        except Exception as e:
            raise e