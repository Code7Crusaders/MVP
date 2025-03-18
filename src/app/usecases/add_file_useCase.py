from abc import ABC, abstractmethod
from models.file_model import FileModel

class AddFileUseCase(ABC):

    @abstractmethod
    def load_file(self, file: FileModel):
        pass
