import pytest
import psycopg2
from datetime import datetime
import pytz

from repositories.template_postgres_repository import TemplatePostgresRepository
from config.db_config import db_config
from entities.template_entity import TemplateEntity


italy_tz = pytz.timezone('Europe/Rome')


@pytest.fixture
def repository():
    """Fixture to create an instance of the repository."""
    return TemplatePostgresRepository(db_config)


def test_database_connection(repository):
    """Test if the database connection is successfully established."""
    try:
        conn = repository._TemplatePostgresRepository__connect()
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 means the connection is open
        conn.close()
    except Exception as e:
        pytest.fail(f"Database connection failed: {e}")


def test_get_template(repository):
    """Test retrieving a template from the database (ensure test data exists)."""
    template_entity = TemplateEntity(id=1)  # get only needs the id
    
    result_template = repository.get_template(template_entity)
    
    assert isinstance(result_template, TemplateEntity)
    assert result_template.get_id() == 1
    assert result_template.get_question() is not None
    assert result_template.get_answer() is not None
    assert result_template.get_author_id() is not None
    assert result_template.get_last_modified() is not None

def test_get_message_none(repository):
    """Test retrieving a non-existing message from the database."""
    template_entity = TemplateEntity(id=-1) # Non-existing ID in your database
    result_message = repository.get_template(template_entity)
    assert result_message is None, "Template not found in database"

def test_get_template_list(repository):
    """Test retrieving all templates from the database."""
    templates = repository.get_template_list()
    
    assert isinstance(templates, list)
    assert all(isinstance(template, TemplateEntity) for template in templates)
    for template in templates:
        assert template.get_id() is not None
        assert template.get_question() is not None
        assert template.get_answer() is not None
        assert template.get_author_id() is not None
        assert template.get_last_modified() is not None
    
def test_save_delete_template(repository):
    """Test saving and deleting a template in the database."""
    try:
        question = "Test question"
        answer = "Test answer"
        author_id = 1  # Replace with a valid author ID in your database
        last_modified = datetime.now(italy_tz)

        template_entity = TemplateEntity(
            question=question,
            answer=answer,
            author_id=author_id,
            last_modified=last_modified
        )

        # Save the template
        saved_id = repository.save_template(template_entity)
        assert saved_id is not None, "Failed to save template"
        template_entity = TemplateEntity(id=saved_id)  # get only needs the id

        # Verify the saved template by retrieving it
        saved_template = repository.get_template(template_entity)  # Pass the instance with the correct id
        assert saved_template is not None, "Saved template not found in database"
        assert saved_template.get_question() == question, "Question mismatch"
        assert saved_template.get_answer() == answer, "Answer mismatch"
        assert saved_template.get_author_id() == author_id, "Author ID mismatch"
        assert saved_template.get_last_modified() == last_modified, "Last modified mismatch"
        assert saved_template.get_id() == saved_id, "ID mismatch"  # Ensure get_id() is called correctly

    except Exception as e:
        pytest.fail(f"Saving template failed: {e}")

    try:
        # Delete the template
        delete_template = TemplateEntity(id=saved_id)
        result = repository.delete_template(delete_template)
        assert result is not None, "Delete function returned None"
        assert isinstance(result, bool), "Delete function did not return a boolean"
        assert result is True, "Failed to delete template"

        # Verify the template is deleted
        deleted_template = repository.get_template(delete_template)  # Pass the instance with the correct id
        assert deleted_template is None, "Template was not deleted"

        # Verify behavior when trying to delete a non-existing template
        non_existing_template = TemplateEntity(id=-1)  # Non-existing ID in your database
        result = repository.delete_template(non_existing_template)
        assert result is not None, "Delete function returned None for non-existing template"
        assert isinstance(result, bool), "Delete function did not return a boolean for non-existing template"
        assert result is False, "Delete function should return False for non-existing template"
    except Exception as e:
        pytest.fail(f"Deleting template failed: {e}")

def test_save_template_fail(repository):
    """Test saving a template with invalid data to ensure it fails."""
    try:
        invalid_template_entity = TemplateEntity(
            question=None,  # Missing question
            answer=None,  # Missing answer
            author_id=None,  # Missing author_id
            last_modified=None  # Missing last_modified
        )
        result = repository.save_template(invalid_template_entity)
        
        assert result is None

        pytest.fail("Saving invalid template should have failed, but it succeeded.")
    except Exception:
        # Expected behavior: an exception should be raised
        pass
