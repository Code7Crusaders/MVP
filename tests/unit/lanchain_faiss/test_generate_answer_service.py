import pytest
from unittest.mock import MagicMock
from app.models.question_model import QuestionModel
from app.models.context_model import ContextModel
from app.models.answer_model import AnswerModel
from app.models.prompt_template_model import PromptTemplateModel
from app.ports.generate_answer_port import GenerateAnswerPort
from app.services.generate_answer_service import GenerateAnswerService

def test_generate_answer():
    # Mock dependencies
    generate_answer_port_mock = MagicMock(spec=GenerateAnswerPort)
    
    prompt_template_model = PromptTemplateModel("You are an ai assistant. You are asked a question and you provide an answer.")

    # Create instance of the service
    service = GenerateAnswerService(generate_answer_port_mock, prompt_template_model)
    
    # Mock input values
    question = QuestionModel(user_id=1, question="What is AI?")
    context = [ContextModel(content="Artificial Intelligence is a field of study.")]
    expected_answer = AnswerModel(answer="AI is a field of study.")
    
    # Configure mock behavior
    generate_answer_port_mock.generate_answer.return_value = expected_answer
    
    # Call the method
    result = service.generate_answer(question, context)
    
    # Assertions
    generate_answer_port_mock.generate_answer.assert_called_once_with(question, context, prompt_template_model)
    assert result == expected_answer

def test_generate_answer_raises_exception():
    # Mock dependencies
    generate_answer_port_mock = MagicMock(spec=GenerateAnswerPort)

    prompt_template_model = PromptTemplateModel("You are an ai assistant. You are asked a question and you provide an answer.")

    # Create instance of the service
    service = GenerateAnswerService(generate_answer_port_mock, prompt_template_model)
    
    # Mock input values
    question = QuestionModel(user_id=1, question="What is AI?")
    context = [ContextModel(content="Artificial Intelligence is a field of study.")]
    
    # Configure mock to raise an exception
    generate_answer_port_mock.generate_answer.side_effect = Exception("Mocked exception")
    
    # Test if exception is raised
    with pytest.raises(Exception, match="An error occurred during the answer generation: Mocked exception"):
        service.generate_answer(question, context)
