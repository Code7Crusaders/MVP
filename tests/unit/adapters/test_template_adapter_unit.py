import pytest
from unittest.mock import MagicMock, ANY
from repositories.template_postgres_repository import TemplatePostgresRepository
from models.template_model import TemplateModel
from adapters.template_postgres_adapter import TemplatePostgresAdapter
from entities.template_entity import TemplateEntity

@pytest.fixture 
def template_postgres_repository_mock():
    return MagicMock(spec=TemplatePostgresRepository)

@pytest.fixture
def template_postgres_adapter(template_postgres_repository_mock: MagicMock):
    return TemplatePostgresAdapter(template_postgres_repository_mock)

# Test get_template

def test_get_template_valid(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Mock repository response
    template_postgres_repository_mock.get_template.return_value = template_model

    result = template_postgres_adapter.get_template(template_model)
    
    assert result.get_id() == 1
    assert result.get_question() == "What is Python?"
    assert result.get_answer() == "A programming language"
    assert result.get_author_id() == 1
    assert result.get_last_modified() == "2025-03-22"

def test_get_template_not_found(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.get_template.side_effect = Exception("Template not found")
    
    with pytest.raises(Exception, match="Template not found"):
        template_postgres_adapter.get_template(template_model)

# Test get_template_list

def test_get_template_list_valid(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    templates = [
        TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22"),
        TemplateModel(id=2, question="What is AI?", answer="Artificial Intelligence", author_id=2, last_modified="2025-03-22")
    ]
    
    # Mock repository response
    template_postgres_repository_mock.get_template_list.return_value = templates

    result = template_postgres_adapter.get_template_list()
    
    assert len(result) == 2
    assert result[0].get_question() == "What is Python?"
    assert result[1].get_question() == "What is AI?"

def test_get_template_list_empty(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    # Mock repository response with no templates
    template_postgres_repository_mock.get_template_list.return_value = []

    result = template_postgres_adapter.get_template_list()
    
    assert result == []

# Test save_template

def test_save_template_valid(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    template_entity = TemplateEntity(
        id=template_model.get_id(),
        question=template_model.get_question(),
        answer=template_model.get_answer(),
        author_id=template_model.get_author_id(),
        last_modified=template_model.get_last_modified()
    )
    
    # Mock repository response
    template_postgres_repository_mock.save_template.return_value = 1  # Return the saved template ID

    result = template_postgres_adapter.save_template(template_model)
    
    template_postgres_repository_mock.save_template.assert_called_once_with(ANY)
    assert result == 1

def test_save_template_failure(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.save_template.side_effect = Exception("Failed to save template")
    
    with pytest.raises(Exception, match="Failed to save template"):
        template_postgres_adapter.save_template(template_model)

# Test delete_template

def test_delete_template_valid(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Mock repository response
    template_postgres_repository_mock.delete_template.return_value = True  # Simulate successful deletion

    result = template_postgres_adapter.delete_template(template_model)
    
    template_postgres_repository_mock.delete_template.assert_called_once_with(ANY)
    assert result is True

def test_delete_template_failure(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.delete_template.side_effect = Exception("Failed to delete template")
    
    with pytest.raises(Exception, match="Failed to delete template"):
        template_postgres_adapter.delete_template(template_model)

# Test get_template_list exception handling

def test_get_template_list_exception(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    # Simulate repository exception
    template_postgres_repository_mock.get_template_list.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        template_postgres_adapter.get_template_list()

# Test get_template exception handling

def test_get_template_exception(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.get_template.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        template_postgres_adapter.get_template(template_model)

# Test save_template exception handling

def test_save_template_exception(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.save_template.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        template_postgres_adapter.save_template(template_model)

# Test delete_template exception handling

def test_delete_template_exception(template_postgres_adapter: TemplatePostgresAdapter, template_postgres_repository_mock: MagicMock):
    template_model = TemplateModel(id=1, question="What is Python?", answer="A programming language", author_id=1, last_modified="2025-03-22")
    
    # Simulate repository exception
    template_postgres_repository_mock.delete_template.side_effect = Exception("Database error")

    with pytest.raises(Exception, match="Database error"):
        template_postgres_adapter.delete_template(template_model)
