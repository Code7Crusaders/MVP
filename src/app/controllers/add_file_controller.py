from app.dto.FileDTO import FileDTO
from app.usecases.add_file_useCase import AddFileUseCase
from app.models.file_model import FileModel


class AddFileController:
    """
    Controller for adding a file to the database.
    """

    def __init__(self, add_file_usecase: AddFileUseCase):
        try:
            self.add_file_usecase = add_file_usecase
        except Exception as e:
            raise e

    def load_file(self, file: FileDTO):
        """
        Add a file to the database.
        """
        try:
            file_model = FileModel(file.get_name(), file.get_path())
            self.add_file_usecase.add_file(file_model)
        except Exception as e:
            raise e
