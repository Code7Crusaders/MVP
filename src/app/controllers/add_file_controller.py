from dto.file_dto import FileDTO
from usecases.add_file_useCase import AddFileUseCase
from models.file_model import FileModel


class AddFileController:
    """
    Controller for adding a file to the database.
    """

    def __init__(self, add_file_usecase: AddFileUseCase):
        
        self.add_file_usecase = add_file_usecase

    def load_file(self, file: FileDTO):
        """
        Add a file to the database.
        Args:
            file (FileDTO): The file data transfer object containing file details.

        Returns:
            None
        """
        try:
            file_model = FileModel(file.get_file_name(), file.get_file_content())
            self.add_file_usecase.load_file(file_model)
        except Exception as e:
            raise e
