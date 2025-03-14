from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.answer_entity import AnswerEntity


class LangChainRepository ():

    def __init__(self):
        pass

    def generate_answer(self, query: QueryEntity, contexts : list[DocumentContextEntity]) -> AnswerEntity:

        pass