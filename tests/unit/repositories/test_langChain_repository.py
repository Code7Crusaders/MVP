import pytest
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from repositories.langChain_repository import LangChainRepository
from entities.query_entity import QueryEntity
from entities.document_context_entity import DocumentContextEntity
from entities.answer_entity import AnswerEntity
from entities.file_entity import FileEntity
from entities.file_chunk_entity import FileChunkEntity

 
load_dotenv()

@pytest.fixture
def langChain_repository():
    

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    model = ChatOpenAI(
        model="gpt-4o-mini", 
        max_tokens=200, 
        temperature=0.5, 
        request_timeout=10
        )
    """
    Model Parameters:
        model (str): The model name to be used, in this case "gpt-4o-mini".
        max_tokens (int): The maximum number of tokens to generate in the response.
        temperature (float): The sampling temperature to use, it indicate the randomness index 0 being no randomness and 1 high randomness, between 0 and 1.
        request_timeout (int): The maximum time in second to wait for a response from the API.
    """

    return LangChainRepository(model)

def test_generate_answer(langChain_repository):
     
    
    prompt_template = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."        
    query = QueryEntity(1, "Hello, What can you tell me about colors?")
    contexts = [
        DocumentContextEntity("Colors are visual perceptual properties corresponding in humans to the categories called red, blue, yellow, green, and others. They are derived from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors."),
        DocumentContextEntity("Color categories and physical specifications of color are associated with objects through the wavelength of the light that is reflected from them."),
        DocumentContextEntity("The perception of color is a subjective process where the brain responds to the stimuli produced when incoming light reacts with the several types of cone cells in the eye.")
    ]

    result = langChain_repository.generate_answer(query, contexts, prompt_template)

    assert result is not None
    assert result.get_answer() is not None
    assert result.get_answer() != ""
    assert isinstance(result, AnswerEntity)

def test_generate_answer_empty_query(langChain_repository):

    prompt_template = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."  

    query = QueryEntity(1, "")
    contexts = [
        DocumentContextEntity("Colors are visual perceptual properties corresponding in humans to the categories called red, blue, yellow, green, and others. They are derived from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors.")
    ]

    with pytest.raises(ValueError, match="Query cannot be empty"):
        langChain_repository.generate_answer(query, contexts, prompt_template)

def test_generate_answer_remember_messages(langChain_repository):
        
    prompt_template = "The following is a conversation with an AI assistant designed to be helpful, creative, and intelligent. It delivers context-aware, concise, and insightful responses while maintaining a professional and engaging tone."
    query1 = QueryEntity(1, "Hello, What can you tell me about colors?")
    contexts1 = [
        DocumentContextEntity("Colors are visual perceptual properties corresponding in humans to the categories called red, blue, yellow, green, and others. They are derived from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors."),
        DocumentContextEntity("Color categories and physical specifications of color are associated with objects through the wavelength of the light that is reflected from them."),
        DocumentContextEntity("The perception of color is a subjective process where the brain responds to the stimuli produced when incoming light reacts with the several types of cone cells in the eye.")
    ]

    result1 = langChain_repository.generate_answer(query1, contexts1, prompt_template)
    assert result1 is not None
    assert result1.get_answer() is not None
    assert result1.get_answer() != ""
    assert isinstance(result1, AnswerEntity)

    query2 = QueryEntity(1, "what was my first question?")
    contexts2 = []

    result2 = langChain_repository.generate_answer(query2, contexts2, prompt_template)
    assert result2 is not None
    assert result2.get_answer() is not None
    assert result2.get_answer() != ""
    assert isinstance(result2, AnswerEntity)

    query5 = QueryEntity(2, "What did you remember I asked in all conversation?")
    contexts5 = []

    result5 = langChain_repository.generate_answer(query5, contexts5, prompt_template)
    assert result5 is not None
    assert result5.get_answer() is not None
    assert result5.get_answer() != ""
    assert isinstance(result5, AnswerEntity)

def test_generate_answer_invalid_contexts(langChain_repository):
    """
    Test generate_answer with invalid contexts to ensure it raises an exception.
    """
    prompt_template = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
    query = QueryEntity(1, "Tell me about colors.")
    contexts = None  # Invalid contexts

    with pytest.raises(Exception, match="Error while generating the answer from LangChain model"):
        langChain_repository.generate_answer(query, contexts, prompt_template)

def test_split_file(langChain_repository):

    file_content = "a" * 2500 + "b" * 2500 + "c" * 2500 + "d" * 2500
    file_metadata = "name.txt"
    file = FileEntity(file_metadata, file_content)
    result = langChain_repository.split_file(file)
    assert result is not None
    assert len(result) == 4
    assert all(isinstance(chunk, FileChunkEntity) for chunk in result)
    assert result[0].get_chunk_content() == "a" * 2500
    assert result[1].get_chunk_content() == "b" * 2500
    assert result[2].get_chunk_content() == "c" * 2500
    assert result[3].get_chunk_content() == "d" * 2500

def test_split_file_empty_content(langChain_repository):
    file_content = ""
    file_metadata = "name.txt"
    file = FileEntity(file_metadata, file_content)
    result = langChain_repository.split_file(file)
    assert result is not None
    assert len(result) == 0
'''
def test_split_file_large_content(langChain_repository):
    
    file_content = "a" * 15001
    file_metadata = "name.txt"
    file = FileEntity(file_metadata, file_content)
    result = langChain_repository.split_file(file)
    assert result is not None
    assert len(result) == 7
    assert all(isinstance(chunk, FileChunkEntity) for chunk in result)
    assert all(chunk.get_chunk_content() == "a" * 2500 for chunk in result)
'''


def test_split_file_with_bytes_content(langChain_repository):
    """
    Test split_file with file content as bytes to ensure it handles decoding properly.
    """
    file_content = ("a" * 2500 + "b" * 2500).encode('utf-8')
    file_metadata = "binary_file.txt"
    file = FileEntity(file_metadata, file_content)
    result = langChain_repository.split_file(file)
    assert result is not None
    assert len(result) == 2
    assert all(isinstance(chunk, FileChunkEntity) for chunk in result)
    assert result[0].get_chunk_content() == "a" * 2500
    assert result[1].get_chunk_content() == "b" * 2500

def test_split_file_exception(langChain_repository):
    """
    Test split_file to ensure it raises an exception for invalid input.
    """
    file_content = None  # Invalid file content
    file_metadata = "invalid_file.txt"
    file = FileEntity(file_metadata, file_content)
    
    with pytest.raises(Exception, match="Error while splitting the file:"):
        langChain_repository.split_file(file)
