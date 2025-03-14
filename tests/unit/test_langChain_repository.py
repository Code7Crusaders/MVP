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

    query3 = QueryEntity(1, "Can you explain the concept of light?")
    contexts3 = [
        DocumentContextEntity("Light is electromagnetic radiation within a certain portion of the electromagnetic spectrum. The word usually refers to visible light, which is the visible spectrum that is visible to the human eye."),
        DocumentContextEntity("Visible light is usually defined as having wavelengths in the range of 400–700 nanometres (nm), between the infrared (with longer wavelengths) and the ultraviolet (with shorter wavelengths).")
    ]

    result3 = langChain_repository.generate_answer(query3, contexts3, prompt_template)
    assert result3 is not None
    assert result3.get_answer() is not None
    assert result3.get_answer() != ""
    assert isinstance(result3, AnswerEntity)

    query4 = QueryEntity(1, "What is the speed of light?")
    contexts4 = [
        DocumentContextEntity("The speed of light in vacuum, commonly denoted c, is a universal physical constant important in many areas of physics. Its exact value is defined as 299,792,458 metres per second (approximately 300,000 km/s or 186,000 mi/s).")
    ]

    result4 = langChain_repository.generate_answer(query4, contexts4, prompt_template)
    assert result4 is not None
    assert result4.get_answer() is not None
    assert result4.get_answer() != ""
    assert isinstance(result4, AnswerEntity)

    query5 = QueryEntity(1, "What did you remember I asked in all conversation?")
    contexts5 = []

    result5 = langChain_repository.generate_answer(query5, contexts5, prompt_template)
    assert result5 is not None
    assert result5.get_answer() is not None
    assert result5.get_answer() != ""
    assert isinstance(result5, AnswerEntity)
    