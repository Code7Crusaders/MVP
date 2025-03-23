import pytest
from unittest.mock import MagicMock
from controllers.delete_template_controller import DeleteTemplateController
from usecases.delete_template_useCase import DeleteTemplateUseCase
from dto.template_dto import TemplateDTO
from models.template_model import TemplateModel

@pytest.fixture
def delete_template_use_case_mock():
    return MagicMock(spec=DeleteTemplateUseCase)

@pytest.fixture
def delete_template_controller(delete_template_use_case_mock):
    return DeleteTemplateController(delete_template_use_case_mock)

# Test delete_template

def test_delete_template_valid(delete_template_controller, delete_template_use_case_mock):
    template_dto = TemplateDTO(id=1, question="Q1", answer="A1", author_id=100, last_modified="2024-03-23")
    delete_template_use_case_mock.delete_template.return_value = True

    result = delete_template_controller.delete_template(template_dto)
    
    assert result is True
    delete_template_use_case_mock.delete_template.assert_called_once()

def test_delete_template_not_found(delete_template_controller, delete_template_use_case_mock):
    template_dto = TemplateDTO(id=-1, question="Q2", answer="A2", author_id=101, last_modified="2024-03-23")
    delete_template_use_case_mock.delete_template.return_value = False

    result = delete_template_controller.delete_template(template_dto)
    
    assert result is False
    delete_template_use_case_mock.delete_template.assert_called_once()

def test_delete_template_exception(delete_template_controller, delete_template_use_case_mock):
    template_dto = TemplateDTO(id=2, question="Q3", answer="A3", author_id=102, last_modified="2024-03-23")
    delete_template_use_case_mock.delete_template.side_effect = Exception("Service error")
    
    with pytest.raises(Exception) as exc_info:
        delete_template_controller.delete_template(template_dto)
    
    assert str(exc_info.value) == "Service error"
    delete_template_use_case_mock.delete_template.assert_called_once()
