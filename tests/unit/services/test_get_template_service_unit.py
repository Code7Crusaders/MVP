import pytest
from unittest.mock import MagicMock
from services.get_template_service import GetTemplateService
from models.template_model import TemplateModel
from ports.get_template_port import GetTemplatePort

@pytest.fixture
def get_template_port_mock():
    return MagicMock(spec=GetTemplatePort)

@pytest.fixture
def get_template_service(get_template_port_mock):
    return GetTemplateService(get_template_port_mock)

# Test get_template

def test_get_template_valid(get_template_service, get_template_port_mock):
    template = TemplateModel(id="1")
    
    # Mock the port method to return the template
    get_template_port_mock.get_template.return_value = template
    
    result = get_template_service.get_template(template)
    
    assert result == template
    get_template_port_mock.get_template.assert_called_once_with(template)

def test_get_template_exception(get_template_service, get_template_port_mock):
    template = TemplateModel(id="1")
    
    # Mock the port method to raise an exception
    get_template_port_mock.get_template.side_effect = Exception("Error retrieving template")
    
    with pytest.raises(Exception) as exc_info:
        get_template_service.get_template(template)
    
    assert "Error retrieving template" in str(exc_info.value)
    get_template_port_mock.get_template.assert_called_once_with(template)
