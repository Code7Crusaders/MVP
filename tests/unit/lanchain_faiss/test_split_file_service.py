import pytest
from unittest.mock import MagicMock
from app.services.add_chunks_service import AddChunksService
from app.ports.add_chunks_port import AddChunksPort
from app.models.file_chunk_model import FileChunkModel

def test_load_chunks_success():
    # Mock dependencies
    add_chunks_port_mock = MagicMock(spec=AddChunksPort)
    service = AddChunksService(add_chunks_port_mock)

    # Create mock chunks
    chunks = [FileChunkModel("chunk content", "metadata")]

    # Call the method
    service.load_chunks(chunks)

    # Assertions
    add_chunks_port_mock.load_chunks.assert_called_once_with(chunks)

def test_load_chunks_exception():
    # Mock dependencies
    add_chunks_port_mock = MagicMock(spec=AddChunksPort)
    service = AddChunksService(add_chunks_port_mock)

    # Create mock chunks
    chunks = [FileChunkModel("chunk content", "metadata")]

    # Simulate an exception
    add_chunks_port_mock.load_chunks.side_effect = Exception("Test Exception")

    # Verify that the exception is propagated
    with pytest.raises(Exception, match="Test Exception"):
        service.load_chunks(chunks)

