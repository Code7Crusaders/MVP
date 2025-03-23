import pytest
from unittest.mock import MagicMock
from controllers.get_template_controller import GetTemplateController
from usecases.get_template_useCase import GetTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

@pytest.fixture
def get_template_use_case_mock():
    return MagicMock(spec=GetTemplateUseCase)

@pytest.fixture
def get_template_controller(get_template_use_case_mock):
    return GetTemplateController(get_template_use_case_mock)

def test_get_template_valid(get_template_controller, get_template_use_case_mock):
    template_dto = TemplateDTO(id="1", question="Q?", answer="A", author_id="123", last_modified="2024-01-01")
    template_model = TemplateModel(id="1", question="Q?", answer="A", author_id="123", last_modified="2024-01-01")

    # Simula il comportamento dell'use case
    get_template_use_case_mock.get_template.return_value = template_model

    result = get_template_controller.get_template(template_dto)

    assert result is not None
    assert result.get_id() == "1"
    assert result.get_question() == "Q?"
    assert result.get_answer() == "A"
    assert result.get_author_id() == "123"
    assert result.get_last_modified() == "2024-01-01"

    get_template_use_case_mock.get_template.assert_called_once()

def test_get_template_not_found(get_template_controller, get_template_use_case_mock):
    template_dto = TemplateDTO(id="1", question="Q?", answer="A", author_id="123", last_modified="2024-01-01")

    # Simula il caso in cui il template non viene trovato
    get_template_use_case_mock.get_template.return_value = None

    result = get_template_controller.get_template(template_dto)

    assert result is None
    get_template_use_case_mock.get_template.assert_called_once()

def test_get_template_exception(get_template_controller, get_template_use_case_mock):
    template_dto = TemplateDTO(id="1", question="Q?", answer="A", author_id="123", last_modified="2024-01-01")

    # Simula un'eccezione generata dall'use case
    get_template_use_case_mock.get_template.side_effect = Exception("Errore nel recupero del template")

    with pytest.raises(Exception) as exc_info:
        get_template_controller.get_template(template_dto)

    assert "Errore nel recupero del template" in str(exc_info.value)
    get_template_use_case_mock.get_template.assert_called_once()
