import pytest
from unittest.mock import MagicMock, patch
from dependencies.init_vector_store import store_vector_store
from langchain_community.vectorstores import FAISS

@pytest.fixture
def mock_vector_store():
    mock_store = MagicMock(spec=FAISS)
    return mock_store


def test_store_vector_store_success(mock_vector_store):
    # Arrange
    with patch('dependencies.init_vector_store.VECTOR_STORE_PATH', '/mock/path/vector_store'):
        with patch.object(mock_vector_store, 'save_local') as mock_save_local:
            # Act
            store_vector_store(mock_vector_store)

            # Assert
            mock_save_local.assert_called_once_with('/mock/path/vector_store')


def test_store_vector_store_prints_path(mock_vector_store, capsys):
    # Arrange
    with patch('dependencies.init_vector_store.VECTOR_STORE_PATH', '/mock/path/vector_store'):
        with patch.object(mock_vector_store, 'save_local'):
            # Act
            store_vector_store(mock_vector_store)

            # Assert
            captured = capsys.readouterr()
            assert "Saved vector store to /mock/path/vector_store" in captured.out


def test_store_vector_store_raises_exception(mock_vector_store):
    # Arrange
    with patch('dependencies.init_vector_store.VECTOR_STORE_PATH', '/mock/path/vector_store'):
        with patch.object(mock_vector_store, 'save_local', side_effect=Exception("Save failed")):
            # Act & Assert
            with pytest.raises(Exception, match="Save failed"):
                store_vector_store(mock_vector_store)