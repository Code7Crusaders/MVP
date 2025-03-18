import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from repositories.template_postgres_repository import TemplatePostgresRepository
from config.db_config import db_config

def test_get_template():
    repo = TemplatePostgresRepository(db_config)
    template = repo.get_template(1)
    if template:
        print(f"Template ID: {template.id}, Question: {template.question}, Answer: {template.answer}, Author: {template.author}, Last Modified: {template.last_modified}")
    else:
        print("Template not found.")

def test_get_template_list():
    repo = TemplatePostgresRepository(db_config)
    templates = repo.get_template_list()
    if templates:
        for template in templates:
            print(f"Template ID: {template.id}, Question: {template.question}, Answer: {template.answer}, Author: {template.author}, Last Modified: {template.last_modified}")
    else:
        print("No templates found.")

def test_save_template():
    repo = TemplatePostgresRepository(db_config)
    try:
        new_template_id = repo.save_template("dio caro", "New Template Answer", "jdoe")
        print(f"New template created with ID: {new_template_id}")
    except ValueError as e:
        print(e)

def test_delete_template():
        repo = TemplatePostgresRepository(db_config)
        try:
            is_deleted = repo.delete_template("jdoe", "come si fanno i cei", "New Template Answer")
            if is_deleted:
                print("Template deleted successfully.")
            else:
                print("Template not found or not deleted.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    test_get_template_list()
    #test_get_template()
    #test_save_template()
    #test_delete_template()


#funziona
