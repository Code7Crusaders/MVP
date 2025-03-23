import pytest
from unittest.mock import MagicMock
from controllers.save_template_controller import SaveTemplateController
from usecases.save_template_useCase import SaveTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

@pytest.fixture
def save_template_use_case_mock():
    return MagicMock(spec=SaveTemplateUseCase)

@pytest.fixture
def save_template_controller(save_template_use_case_mock):
    return SaveTemplateController(save_template_use_case_mock)

def test_save_template_valid(save_template_controller, save_template_use_case_mock):
    template_dto = TemplateDTO(
        id="1",
        question="What is the capital of France?",
        answer="Paris",
        author_id="123",
        last_modified="2024-01-01"
    )

    # Simula il comportamento dell'use case per restituire un ID
    save_template_use_case_mock.save_template.return_value = 1

    result = save_template_controller.save_template(template_dto)

    assert result == 1
    save_template_use_case_mock.save_template.assert_called_once()

def test_save_template_exception(save_template_controller, save_template_use_case_mock):
    template_dto = TemplateDTO(
        id="1",
        question="What is the capital of France?",
        answer="Paris",
        author_id="123",
        last_modified="2024-01-01"
    )

    # Simula un'eccezione generata dall'use case
    save_template_use_case_mock.save_template.side_effect = Exception("Errore durante il salvataggio del template")

    with pytest.raises(Exception) as exc_info:
        save_template_controller.save_template(template_dto)

    assert "Errore durante il salvataggio del template" in str(exc_info.value)
    save_template_use_case_mock.save_template.assert_called_once()
