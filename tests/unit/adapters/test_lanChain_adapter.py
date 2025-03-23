from unittest.mock import MagicMock, ANY
import pytest
from adapters.langChain_adapter import LangChainAdapter
from models.answer_model import AnswerModel
from models.context_model import ContextModel
from models.question_model import QuestionModel
from models.file_chunk_model import FileChunkModel
from models.file_model import FileModel
from models.prompt_template_model import PromptTemplateModel

def test_generate_answer_valid():
    # Mock the repository
    lang_chain_repository_mock = MagicMock()
    lang_chain_adapter = LangChainAdapter(lang_chain_repository_mock)

    # Test inputs
    question = QuestionModel(user_id=123, question="What is AI?")
    context = [ContextModel("Artificial Intelligence is a field of study.")]
    prompt_template = PromptTemplateModel("Answer the question using the given context:")

    # Mock repository response
    mock_answer_entity = MagicMock()
    mock_answer_entity.get_answer.return_value = "AI is a field of study focused on creating intelligent machines."
    lang_chain_repository_mock.generate_answer.return_value = mock_answer_entity

    # Call the method
    result = lang_chain_adapter.generate_answer(question, context, prompt_template)

    # Assertions
    assert isinstance(result, AnswerModel)
    assert result.get_answer() == "AI is a field of study focused on creating intelligent machines."

    lang_chain_repository_mock.generate_answer.assert_called_once_with(
        ANY,  
        ANY,  
        "Answer the question using the given context:"
    )


def test_split_file_valid():
    # Mock the repository
    lang_chain_repository_mock = MagicMock()
    lang_chain_adapter = LangChainAdapter(lang_chain_repository_mock)

    # Test input
    file = FileModel("test.txt", "This is a test file content.")

    # Mock repository response
    mock_chunk_1 = MagicMock()
    mock_chunk_1.get_chunk_content.return_value = "This is a"
    mock_chunk_1.get_metadata.return_value = "Chunk 1 metadata"

    mock_chunk_2 = MagicMock()
    mock_chunk_2.get_chunk_content.return_value = "test file content."
    mock_chunk_2.get_metadata.return_value = "Chunk 2 metadata"

    lang_chain_repository_mock.split_file.return_value = [mock_chunk_1, mock_chunk_2]

    # Call the method
    result = lang_chain_adapter.split_file(file)

    # Assertions
    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], FileChunkModel)
    assert result[0].get_chunk_content() == "This is a"
    assert result[0].get_metadata() == "Chunk 1 metadata"
    assert isinstance(result[1], FileChunkModel)
    assert result[1].get_chunk_content() == "test file content."
    assert result[1].get_metadata() == "Chunk 2 metadata"

    lang_chain_repository_mock.split_file.assert_called_once_with(ANY)

