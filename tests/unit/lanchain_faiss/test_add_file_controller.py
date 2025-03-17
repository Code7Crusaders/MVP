import pytest
from unittest.mock import MagicMock, ANY
from app.controllers.add_file_controller import AddFileController
from app.dto.FileDTO import FileDTO
from app.usecases.add_file_useCase import AddFileUseCase
from app.models.file_model import FileModel


@pytest.fixture
def mock_add_file_usecase():
    return MagicMock(spec=AddFileUseCase)


@pytest.fixture
def add_file_controller(mock_add_file_usecase):
    return AddFileController(mock_add_file_usecase)


def test_load_file_success(add_file_controller, mock_add_file_usecase):
    """
    Test to verify that load_file correctly converts FileDTO to FileModel
    and calls the use case method.
    """
    # Arrange
    file_dto = FileDTO("test.txt", "File content")
    
    # Act
    add_file_controller.load_file(file_dto)

    # Assert
    mock_add_file_usecase.load_file.assert_called_once_with(ANY)
    
    
    called_arg = mock_add_file_usecase.load_file.call_args[0][0]
    assert called_arg.filename == "test.txt"
    assert called_arg.file_content == "File content"

def test_load_file_failure(add_file_controller, mock_add_file_usecase):
    """
    Test to verify that load_file raises an exception when the use case method fails.
    """
    # Arrange
    file_dto = FileDTO("test.txt", "File content")
    mock_add_file_usecase.load_file.side_effect = Exception("Failed to load file")

    # Act & Assert
    with pytest.raises(Exception, match="Failed to load file"):
        add_file_controller.load_file(file_dto)

