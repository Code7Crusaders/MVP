import pytest
from unittest.mock import MagicMock
from services.split_file_service import SplitFileService
from ports.split_file_port import SplitFilePort
from models.file_model import FileModel
from models.file_chunk_model import FileChunkModel

def test_split_file_success():
    # Mock dependencies
    split_file_port_mock = MagicMock(spec=SplitFilePort)
    service = SplitFileService(split_file_port_mock)

    # Create mock input and output
    file = FileModel("test_file.txt", "file content")
    expected_chunks = [
        FileChunkModel("chunk1", "metadata1"),
        FileChunkModel("chunk2", "metadata2"),
    ]
    
    # Mock behavior
    split_file_port_mock.split_file.return_value = expected_chunks

    # Call the method
    result = service.split_file(file)

    # Assertions
    split_file_port_mock.split_file.assert_called_once_with(file)
    assert result == expected_chunks

def test_split_file_exception():
    # Mock dependencies
    split_file_port_mock = MagicMock(spec=SplitFilePort)
    service = SplitFileService(split_file_port_mock)

    # Create mock input
    file = FileModel("test_file.txt", "file content")

    # Simulate an exception
    split_file_port_mock.split_file.side_effect = Exception("Split error")

    # Verify that the exception is propagated
    with pytest.raises(Exception, match="Split error"):
        service.split_file(file)
