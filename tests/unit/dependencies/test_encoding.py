import pytest
from unittest.mock import mock_open, patch
from dependencies.encoding import detect_encoding

def test_detect_encoding_valid_file():
    # Arrange
    mock_file_content = b'This is a test file with UTF-8 encoding.'
    mock_chardet_result = {'encoding': 'utf-8'}
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as mocked_file:
        with patch('chardet.detect', return_value=mock_chardet_result) as mocked_chardet:
            # Act
            encoding = detect_encoding('test_file.txt')

            # Assert
            mocked_file.assert_called_once_with('test_file.txt', 'rb')
            mocked_chardet.assert_called_once_with(mock_file_content)
            assert encoding == 'utf-8'


def test_detect_encoding_empty_file():
    # Arrange
    mock_file_content = b''
    mock_chardet_result = {'encoding': None}
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as mocked_file:
        with patch('chardet.detect', return_value=mock_chardet_result) as mocked_chardet:
            # Act
            encoding = detect_encoding('empty_file.txt')

            # Assert
            mocked_file.assert_called_once_with('empty_file.txt', 'rb')
            mocked_chardet.assert_called_once_with(mock_file_content)
            assert encoding is None


def test_detect_encoding_partial_read():
    # Arrange
    mock_file_content = b'A' * 100000  # Simulate a file with 100,000 bytes
    mock_chardet_result = {'encoding': 'ascii'}
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as mocked_file:
        with patch('chardet.detect', return_value=mock_chardet_result) as mocked_chardet:
            # Act
            encoding = detect_encoding('large_file.txt')

            # Assert
            mocked_file.assert_called_once_with('large_file.txt', 'rb')
            mocked_chardet.assert_called_once_with(mock_file_content)
            assert encoding == 'ascii'


def test_detect_encoding_raises_file_not_found_error():
    # Arrange
    with patch('builtins.open', side_effect=FileNotFoundError):
        # Act & Assert
        with pytest.raises(FileNotFoundError):
            detect_encoding('non_existent_file.txt')


def test_detect_encoding_raises_permission_error():
    # Arrange
    with patch('builtins.open', side_effect=PermissionError):
        # Act & Assert
        with pytest.raises(PermissionError):
            detect_encoding('restricted_file.txt')