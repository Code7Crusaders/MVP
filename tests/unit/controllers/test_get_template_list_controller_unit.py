import pytest
from unittest.mock import MagicMock
from controllers.get_template_list_controller import GetTemplateListController
from usecases.get_template_list_useCase import GetTemplateListUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

@pytest.fixture
def get_template_list_use_case_mock():
    return MagicMock(spec=GetTemplateListUseCase)

@pytest.fixture
def get_template_list_controller(get_template_list_use_case_mock):
    return GetTemplateListController(get_template_list_use_case_mock)

def test_get_template_list_valid(get_template_list_controller, get_template_list_use_case_mock):
    templates_model = [
        TemplateModel(id="1", question="Q1?", answer="A1", author_id="123", last_modified="2024-01-01"),
        TemplateModel(id="2", question="Q2?", answer="A2", author_id="456", last_modified="2024-01-02"),
    ]

    # Simula il comportamento dell'use case
    get_template_list_use_case_mock.get_template_list.return_value = templates_model

    result = get_template_list_controller.get_template_list()

    assert len(result) == 2
    assert result[0].get_id() == "1"
    assert result[1].get_id() == "2"

    get_template_list_use_case_mock.get_template_list.assert_called_once()

def test_get_template_list_empty(get_template_list_controller, get_template_list_use_case_mock):
    # Simula il caso in cui non ci sono template
    get_template_list_use_case_mock.get_template_list.return_value = []

    result = get_template_list_controller.get_template_list()

    assert result == []
    get_template_list_use_case_mock.get_template_list.assert_called_once()

def test_get_template_list_exception(get_template_list_controller, get_template_list_use_case_mock):
    # Simula un'eccezione generata dall'use case
    get_template_list_use_case_mock.get_template_list.side_effect = Exception("Errore nel recupero dei template")

    with pytest.raises(Exception) as exc_info:
        get_template_list_controller.get_template_list()

    assert "Errore nel recupero dei template" in str(exc_info.value)
    get_template_list_use_case_mock.get_template_list.assert_called_once()
