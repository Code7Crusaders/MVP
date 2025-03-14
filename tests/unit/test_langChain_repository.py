import pytest
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.repositories.langChain_repository import LangChainRepository
from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.answer_entity import AnswerEntity
from app.entities.file_entity import FileEntity
from app.entities.file_chunk_entity import FileChunkEntity


load_dotenv()

@pytest.fixture
def langChain_repository():
    

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    model = ChatOpenAI(
        model="gpt-4o-mini", 
        max_tokens=2000, 
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
     
    query = QueryEntity(1, "Hello, What can you tell me about colors?")
    contexts = [
        DocumentContextEntity("Colors are visual perceptual properties corresponding in humans to the categories called red, blue, yellow, green, and others. They are derived from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors."),
        DocumentContextEntity("Color categories and physical specifications of color are associated with objects through the wavelength of the light that is reflected from them."),
        DocumentContextEntity("The perception of color is a subjective process where the brain responds to the stimuli produced when incoming light reacts with the several types of cone cells in the eye.")
    ]

    result = langChain_repository.generate_answer(query, contexts)

    assert result is not None
    assert result.get_answer() is not None
    assert result.get_answer() != ""
    assert isinstance(result, AnswerEntity)

def test_generate_answer_empty_query(langChain_repository):
    query = QueryEntity(1, "")
    contexts = [
        DocumentContextEntity("Colors are visual perceptual properties corresponding in humans to the categories called red, blue, yellow, green, and others. They are derived from the spectrum of light interacting in the eye with the spectral sensitivities of the light receptors.")
    ]
    
    with pytest.raises(ValueError, match="Query cannot be empty"):
        langChain_repository.generate_answer(query, contexts)

