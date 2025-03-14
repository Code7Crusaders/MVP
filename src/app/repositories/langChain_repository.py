from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.answer_entity import AnswerEntity
from app.entities.file_entity import FileEntity
from app.entities.file_chunk_entity import FileChunkEntity


class LangChainRepository ():

    def __init__(self):
        pass

    def generate_answer(self, query: QueryEntity, contexts : list[DocumentContextEntity]) -> AnswerEntity:

        pass

    def split_file(self, file: FileEntity) -> list[FileChunkEntity]:
        
        pass