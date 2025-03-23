import pytest
from unittest.mock import MagicMock
from services.get_template_list_service import GetTemplateListService
from models.template_model import TemplateModel
from ports.get_template_list_port import GetTemplateListPort

@pytest.fixture
def get_template_list_port_mock():
    return MagicMock(spec=GetTemplateListPort)

@pytest.fixture
def get_template_list_service(get_template_list_port_mock):
    return GetTemplateListService(get_template_list_port_mock)

# Test get_template_list

def test_get_template_list_valid(get_template_list_service, get_template_list_port_mock):
    templates = [
        TemplateModel(id="1"),
        TemplateModel(id="2"),
    ]
    
    # Mock the port method to return a list of templates
    get_template_list_port_mock.get_template_list.return_value = templates
    
    result = get_template_list_service.get_template_list()
    
    assert result == templates
    get_template_list_port_mock.get_template_list.assert_called_once()

def test_get_template_list_no_templates(get_template_list_service, get_template_list_port_mock):
    templates = []  # Empty list for no templates
    
    # Mock the port method to return an empty list
    get_template_list_port_mock.get_template_list.return_value = templates
    
    result = get_template_list_service.get_template_list()
    
    assert result == templates
    get_template_list_port_mock.get_template_list.assert_called_once()

def test_get_template_list_exception(get_template_list_service, get_template_list_port_mock):
    # Mock the port method to raise an exception
    get_template_list_port_mock.get_template_list.side_effect = Exception("Error retrieving templates")
    
    with pytest.raises(Exception) as exc_info:
        get_template_list_service.get_template_list()
    
    assert "Error retrieving templates" in str(exc_info.value)
    get_template_list_port_mock.get_template_list.assert_called_once()

