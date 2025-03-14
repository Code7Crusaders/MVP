from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document

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

        if not query.get_query().strip():
            raise ValueError("Query cannot be empty")

        try: 
            user_question = query.get_query()
            default_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
            documents = [Document(page_content=context.get_content()) for context in contexts]

            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ("system", "{default_prompt}"),
                    ("user", "{user_question}"),
                    ("system", "{context}")  
                ]
            )

            chain = create_stuff_documents_chain(
                llm=self.model,
                prompt=prompt_template
            )

            answer = chain.invoke({
                "default_prompt": default_prompt,  
                "user_question": user_question,  
                "context": documents  
            })

            return AnswerEntity(answer)

        except Exception as e:
            raise Exception("Error while generating the answer from LangChain model: " + str(e))



    def split_file(self, file: FileEntity) -> list[FileChunkEntity]:
        
        pass