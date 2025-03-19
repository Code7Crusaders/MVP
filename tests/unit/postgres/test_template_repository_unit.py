import pytest
from unittest.mock import patch, MagicMock
from repositories.template_postgres_repository import TemplatePostgresRepository
from config.db_config import db_config

@pytest.fixture
def template_repo():
    return TemplatePostgresRepository(db_config)

@patch('repositories.template_postgres_repository.TemplatePostgresRepository.get_template')
def test_get_template(mock_get_template, template_repo):
    mock_template = MagicMock()
    mock_template.id = 1
    mock_template.question = "Test Question"
    mock_template.answer = "Test Answer"
    mock_template.author = "Test Author"
    mock_template.last_modified = "2023-10-01"
    mock_get_template.return_value = mock_template

    template = template_repo.get_template(1)
    
    assert template is not None
    assert template.id == 1
    assert template.question == "Test Question"
    assert template.answer == "Test Answer"
    assert template.author == "Test Author"
    assert template.last_modified == "2023-10-01"

@patch('repositories.template_postgres_repository.TemplatePostgresRepository.save_template')
def test_save_template(mock_save_template, template_repo):
    mock_save_template.return_value = 1

    new_template_id = template_repo.save_template("Test Question", "Test Answer", "Test Author")
    
    assert new_template_id == 1
    mock_save_template.assert_called_once_with("Test Question", "Test Answer", "Test Author")

@patch('repositories.template_postgres_repository.TemplatePostgresRepository.delete_template')
def test_delete_template(mock_delete_template, template_repo):
    mock_delete_template.return_value = True

    is_deleted = template_repo.delete_template("Test Author", "Test Question", "Test Answer")
    
    assert is_deleted is True
    mock_delete_template.assert_called_once_with("Test Author", "Test Question", "Test Answer")
