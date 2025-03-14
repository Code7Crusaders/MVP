from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.answer_entity import AnswerEntity
from app.entities.file_entity import FileEntity
from app.entities.file_chunk_entity import FileChunkEntity


class LangChainRepository ():

    def __init__(self, model: ChatOpenAI):
        self.model = model

    def generate_answer(self, query: QueryEntity, contexts : list[DocumentContextEntity]) -> AnswerEntity:
        """
        Given a Query and a list of document contexts it perform a call to OpenAi LLM model and get a detailed answer

        Args:
            query (QueryEntity): The query entity containing the question.
            contexts (list[DocumentContextEntity]): A list of document context entities.
        
        Returns:
            AnswerEntity: A detailed answer entity containing the answer given by LLM.

        Raises:
            Exception: If an error occurs during the answer generation.
        """

        try: 
            user_question = query.get_question()
            

            prompt = ChatPromptTemplate(
                [("user", "{user_question}\n\n{}\n\n{}")] +
            )



    def split_file(self, file: FileEntity) -> list[FileChunkEntity]:
        
        pass