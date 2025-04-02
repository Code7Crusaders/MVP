import pytest
from unittest.mock import MagicMock
from controllers.update_message_rating_controller import UpdateMessageRatingController
from usecases.update_message_rating_useCase import UpdateMessageRatingUseCase
from dto.message_dto import MessageDTO

@pytest.fixture
def mock_update_message_rating_use_case():
    return MagicMock(spec=UpdateMessageRatingUseCase)


@pytest.fixture
def update_message_rating_controller(mock_update_message_rating_use_case):
    return UpdateMessageRatingController(mock_update_message_rating_use_case)


@pytest.fixture
def mock_message_dto():
    mock_dto = MagicMock(spec=MessageDTO)
    mock_dto.get_id.return_value = 1
    mock_dto.get_rating.return_value = 4.5
    return mock_dto


def test_update_message_rating_success(update_message_rating_controller, mock_update_message_rating_use_case, mock_message_dto):
    # Arrange
    mock_update_message_rating_use_case.update_message_rating.return_value = True

    # Act
    result = update_message_rating_controller.update_message_rating(mock_message_dto)

    # Assert
    assert result is True
    mock_update_message_rating_use_case.update_message_rating.assert_called_once()


def test_update_message_rating_failure(update_message_rating_controller, mock_update_message_rating_use_case, mock_message_dto):
    # Arrange
    mock_update_message_rating_use_case.update_message_rating.return_value = False

    # Act
    result = update_message_rating_controller.update_message_rating(mock_message_dto)

    # Assert
    assert result is False
    mock_update_message_rating_use_case.update_message_rating.assert_called_once()


def test_update_message_rating_raises_exception(update_message_rating_controller, mock_update_message_rating_use_case, mock_message_dto):
    # Arrange
    mock_update_message_rating_use_case.update_message_rating.side_effect = Exception("Update failed")

    # Act & Assert
    with pytest.raises(Exception, match="Update failed"):
        update_message_rating_controller.update_message_rating(mock_message_dto)
    mock_update_message_rating_use_case.update_message_rating.assert_called_once()