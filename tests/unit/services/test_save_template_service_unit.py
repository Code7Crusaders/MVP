import pytest
from unittest.mock import MagicMock
from services.save_template_service import SaveTemplateService
from models.template_model import TemplateModel
from ports.save_template_port import SaveTemplatePort

@pytest.fixture
def save_template_port_mock():
    return MagicMock(spec=SaveTemplatePort)

@pytest.fixture
def save_template_service(save_template_port_mock):
    return SaveTemplateService(save_template_port_mock)

# Test save_template

def test_save_template_valid(save_template_service, save_template_port_mock):
    template = TemplateModel(id="1")
    saved_template_id = 123  # Mock the saved template's ID
    
    # Mock the port method to return the ID of the saved template
    save_template_port_mock.save_template.return_value = saved_template_id
    
    result = save_template_service.save_template(template)
    
    assert result == saved_template_id
    save_template_port_mock.save_template.assert_called_once_with(template)

def test_save_template_exception(save_template_service, save_template_port_mock):
    template = TemplateModel(id="1")
    
    # Mock the port method to raise an exception
    save_template_port_mock.save_template.side_effect = Exception("Error saving template")
    
    with pytest.raises(Exception) as exc_info:
        save_template_service.save_template(template)
    
    assert "Error saving template" in str(exc_info.value)
    save_template_port_mock.save_template.assert_called_once_with(template)
