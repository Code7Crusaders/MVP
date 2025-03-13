from abc import ABC, abstractmethod
from app.models.file_chunk_model import FileModel

class AddFileUseCase(ABC):

    @abstractmethod
    def load_file(self, file: FileModel):
        pass
