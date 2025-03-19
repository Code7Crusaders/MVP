import pytest
import psycopg2
from unittest.mock import patch, MagicMock


from models.template_model import TemplateModel 
from repositories.template_postgres_repository import TemplatePostgresRepository
from entities.template_entity import TemplateEntity
from config.db_config import db_config


@pytest.fixture
def template_repo():
    """Fixture to create an instance of the repository."""
    return TemplatePostgresRepository(db_config)

def test_database_connection(template_repo):
    """Test if the database connection is successfully established."""
    try:
        conn = template_repo._TemplatePostgresRepository__connect() 
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")

def test_get_template(template_repo):
    """Test retrieving a template from the database (ensure test data exists)."""
    template_id = 1  # existing ID of template in your DB
    template = template_repo.get_template(template_id)
    assert template is not None, "Template not found in database"
    assert isinstance(template, TemplateEntity)

def test_get_template_none(template_repo):
    """Test retrieving a non-existing template from the database."""
    template_id = -1  # non-existing ID of template in your DB
    template = template_repo.get_template(template_id)
    assert template is None, "Template found in database"

def test_get_template_list(template_repo):
    """Test retrieving all templates from the database."""
    templates = template_repo.get_template_list()
    assert isinstance(templates, list)
    if templates:  
        assert all(isinstance(template, TemplateEntity) for template in templates), "All items should be TemplateEntity instances"

def test_save_template(template_repo):
    """Test saving a template to the database."""
    question = "Test Question"
    author = 2 # enshure that this user exists in your database
    answer = "Test answer jokerigno lesgo"

    try:
        template_id = template_repo.save_template(question, answer, author)
        
        assert template_id is not None, "Failed to save template"
        assert isinstance(template_id, int), "Template ID should be an integer"
    except Exception as e:
        pytest.fail(f"Failed to save template: {e}")

    """Test deleting a template from the database."""

    try:
        is_deleted = template_repo.delete_template(template_id)
        
        assert is_deleted is True, "Failed to delete template"
    except Exception as e:
        pytest.fail(f"Failed to delete template: {e}")


def test_save_template_author_not_exists(template_repo):
    """Test saving a template with a non-existing author."""
    question = "Test Question"
    answer = "Test Answer"
    non_existing_author = -1  # ID of a non-existing author
    
    with pytest.raises(ValueError, match=f"Author '{non_existing_author}' does not exist in the Users table."):
        template_repo.save_template(question, answer, non_existing_author)


def test_save_template_already_exists(template_repo):
    """Test saving a template that already exists in the database."""
    question = "Duplicate Question"
    answer = "Duplicate Answer"
    existing_author = 2  # Ensure this author exists in your database

    # Save the template for the first time
    templates = template_repo.get_template_list()
    for template in templates:
        if template.get_question() == question and template.get_answer() == answer and template.get_author() == existing_author:
            break
    else:
        try:
            template_repo.save_template(question, answer, existing_author)
        except Exception as e:
            pytest.fail(f"Failed to save initial template: {e}")

    # Attempt to save the same template again
    with pytest.raises(ValueError, match="A template with the same question, answer, and author already exists."):
        template_repo.save_template(question, answer, existing_author)


def test_delete_template_not_found(template_repo):
    """Test deleting a non-existing template from the database."""
    non_existing_template_id = -1  # ID of a non-existing template

    try:
        is_deleted = template_repo.delete_template(non_existing_template_id)
        assert is_deleted is False, "Expected False when deleting a non-existing template"
    except Exception as e:
        pytest.fail(f"Failed to handle deletion of non-existing template: {e}")

