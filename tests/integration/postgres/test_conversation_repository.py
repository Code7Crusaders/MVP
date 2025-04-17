import pytest
import psycopg2
from entities.conversation_entity import ConversationEntity
from repositories.conversation_postgres_repository import ConversationPostgresRepository
from config.db_config import db_config


@pytest.fixture
def repository():
    """Fixture per creare un'istanza del repository."""
    return ConversationPostgresRepository(db_config)


def test_database_connection(repository):
    """Test per verificare se la connessione al database è stabilita correttamente."""
    try:
        conn = repository._ConversationPostgresRepository__connect()
        assert conn is not None
        assert isinstance(conn, psycopg2.extensions.connection)
        assert conn.closed == 0  # 0 indica che la connessione è aperta
        conn.close()
    except Exception as e:
        pytest.fail(f"Connessione al database fallita: {e}")


def test_get_conversation(repository):
    """Test per recuperare una conversazione dal database (assicurati che esista un test ID valido)."""
    conversation_entity = ConversationEntity(id=1)  # Fornisci un ID esistente
    result_conversation = repository.get_conversation(conversation_entity)
    
    assert isinstance(result_conversation, ConversationEntity)
    assert result_conversation.get_id() == 1
    assert result_conversation.get_title() is not None
    assert result_conversation.get_user_id() is not None


def test_get_conversation_error(repository):
    """Test per recuperare una conversazione non esistente dal database."""
    conversation_entity = ConversationEntity(id=-1)  # ID non esistente
    result_conversation = repository.get_conversation(conversation_entity)
    assert result_conversation is None


def test_get_conversations(repository):
    """Test per recuperare tutte le conversazioni associate a un utente."""
    user_id = 1  # Fornisci un ID utente valido
    dummy_conversation = ConversationEntity(user_id=user_id)
    result_conversations = repository.get_conversations(dummy_conversation)

    assert isinstance(result_conversations, list)
    assert len(result_conversations) > 0  # Assicurati che ci siano conversazioni associate
    for conversation in result_conversations:
        assert isinstance(conversation, ConversationEntity)
        assert conversation.get_user_id() == user_id


def test_save_delete_conversation(repository):
    """Test per salvare e cancellare una conversazione nel database."""
    try:
        title = "Test Conversation"
        user_id = 1  # Fornisci un ID utente valido
        conversation_entity = ConversationEntity(title=title, user_id=user_id)

        # Salva la conversazione
        saved_id = repository.save_conversation_title(conversation_entity)
        assert saved_id is not None, "Fallimento nel salvataggio della conversazione"

        # Recupera la conversazione salvata
        saved_conversation = repository.get_conversation(ConversationEntity(id=saved_id))
        assert saved_conversation is not None, "La conversazione salvata non è stata trovata nel database"
        assert saved_conversation.get_title() == title, "Mismatch nel titolo"
        assert saved_conversation.get_user_id() == user_id, "Mismatch nell'utente associato"

        # Cancella la conversazione
        delete_result = repository.delete_conversation(ConversationEntity(id=saved_id))
        assert delete_result is True, "Fallimento nella cancellazione della conversazione"

        # Verifica che la conversazione sia stata cancellata
        deleted_conversation = repository.get_conversation(ConversationEntity(id=saved_id))
        assert deleted_conversation is None, "La conversazione non è stata cancellata correttamente"

    except Exception as e:
        pytest.fail(f"Errore nei test di salvataggio/cancellazione della conversazione: {e}")


def test_save_conversation_invalid_data(repository):
    """Test per verificare che il salvataggio di dati non validi fallisca."""
    try:
        invalid_conversation_entity = ConversationEntity(title=None, user_id=None)  # Dati non validi
        saved_id = repository.save_conversation_title(invalid_conversation_entity)
        pytest.fail("Il salvataggio di una conversazione con dati non validi avrebbe dovuto fallire, ma ha avuto successo.")
    except Exception:
        # Comportamento atteso: deve essere sollevata un'eccezione
        pass
