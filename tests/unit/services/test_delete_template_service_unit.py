import pytest
from unittest.mock import MagicMock
from services.delete_template_service import DeleteTemplateService
from ports.delete_template_port import DeleteTemplatePort
from models.template_model import TemplateModel

@pytest.fixture
def delete_template_port_mock():
    return MagicMock(spec=DeleteTemplatePort)

@pytest.fixture
def delete_template_service(delete_template_port_mock):
    return DeleteTemplateService(delete_template_port_mock)

# Test delete_template

def test_delete_template_valid(delete_template_service, delete_template_port_mock):
    template = TemplateModel(id=1)
    delete_template_port_mock.delete_template.return_value = True

    result = delete_template_service.delete_template(template)
    
    assert result is True
    delete_template_port_mock.delete_template.assert_called_once_with(template)

def test_delete_template_not_found(delete_template_service, delete_template_port_mock):
    template = TemplateModel(id=-1)
    delete_template_port_mock.delete_template.return_value = False

    result = delete_template_service.delete_template(template)
    
    assert result is False
    delete_template_port_mock.delete_template.assert_called_once_with(template)

def test_delete_template_exception(delete_template_service, delete_template_port_mock):
    template = TemplateModel(id=2)
    delete_template_port_mock.delete_template.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        delete_template_service.delete_template(template)
    
    assert str(exc_info.value) == "Database error"
    delete_template_port_mock.delete_template.assert_called_once_with(template)