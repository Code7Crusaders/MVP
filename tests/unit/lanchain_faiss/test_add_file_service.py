import pytest
from unittest.mock import MagicMock
from app.services.add_file_service import AddFileService
from app.services.split_file_service import SplitFileService
from app.services.add_chunks_service import AddChunksService
from app.models.file_model import FileModel
from app.models.file_chunk_model import FileChunkModel


def test_load_file_success():
    """
    Test successful file processing.
    """
    split_file_service_mock = MagicMock(spec=SplitFileService)
    add_chunks_service_mock = MagicMock(spec=AddChunksService)
    service = AddFileService(split_file_service_mock, add_chunks_service_mock)

    file = FileModel("test_file.txt", "file content")
    chunks = [
        FileChunkModel("chunk1", "metadata1"),
        FileChunkModel("chunk2", "metadata2"),
    ]

    split_file_service_mock.split_file.return_value = chunks
    add_chunks_service_mock.load_chunks.return_value = None

    service.load_file(file)

    # Assertions
    split_file_service_mock.split_file.assert_called_once_with(file)
    add_chunks_service_mock.load_chunks.assert_called_once_with(chunks)


def test_load_file_split_exception():
    """
    Test exception handling when split_file fails.
    """
    split_file_service_mock = MagicMock(spec=SplitFileService)
    add_chunks_service_mock = MagicMock(spec=AddChunksService)
    service = AddFileService(split_file_service_mock, add_chunks_service_mock)

    file = FileModel("test_file.txt", "file content")

    split_file_service_mock.split_file.side_effect = Exception("Split error")

    with pytest.raises(Exception, match="Split error"):
        service.load_file(file)

    # Ensure that load_chunks was never called
    add_chunks_service_mock.load_chunks.assert_not_called()


def test_load_file_add_chunks_exception():
    """
    Test exception handling when load_chunks fails.
    """
    split_file_service_mock = MagicMock(spec=SplitFileService)
    add_chunks_service_mock = MagicMock(spec=AddChunksService)
    service = AddFileService(split_file_service_mock, add_chunks_service_mock)

    file = FileModel("test_file.txt", "file content")
    chunks = [
        FileChunkModel("chunk1", "metadata1"),
        FileChunkModel("chunk2", "metadata2"),
    ]

    split_file_service_mock.split_file.return_value = chunks
    add_chunks_service_mock.load_chunks.side_effect = Exception("Add chunks error")

    with pytest.raises(Exception, match="Add chunks error"):
        service.load_file(file)

    # Ensure split_file was called, but load_chunks raised an error
    split_file_service_mock.split_file.assert_called_once_with(file)
    add_chunks_service_mock.load_chunks.assert_called_once_with(chunks)
