from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain_core.messages import trim_messages
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory

from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.answer_entity import AnswerEntity
from app.entities.file_entity import FileEntity
from app.entities.file_chunk_entity import FileChunkEntity


class LangChainRepository:
    def __init__(self, model: ChatOpenAI):
        try:
            self.model = model
            self.user_memories = {}  
        except Exception as e:
            raise Exception("Error while initializing LangChain model: " + str(e))

    def get_user_memory(self, user_id: int):
        """Retrieve or create memory for a specific user."""
        if user_id not in self.user_memories:
            self.user_memories[user_id] = ConversationBufferMemory(return_messages=True)
        return self.user_memories[user_id]
    
    def generate_answer(self, query: QueryEntity, contexts: list[DocumentContextEntity], prompt_template: str) -> AnswerEntity:
        """
        Given a Query and a list of document contexts, perform a call to the OpenAI LLM model and get a detailed answer.

        Args:
            user_id (int): The unique identifier of the user.
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
            documents = [Document(page_content=context.get_content()) for context in contexts]

            # Get user-specific memory
            memory = self.get_user_memory(query.get_user_id())
            history = memory.load_memory_variables({})["history"]

            # Trim history if needed
            trimmed_history = trim_messages(
                history,
                max_tokens=200,
                strategy="last",
                include_system=True,
                token_counter=self.model
            )

            history_message = f"Previous conversation history: {''.join(msg.content for msg in trimmed_history) if isinstance(trimmed_history, list) else str(trimmed_history)}"

            # **Ensure history is used in the prompt**
            prompt_template = ChatPromptTemplate.from_messages(
                [
                    ("system", prompt_template),
                    ("system", history_message),  
                    ("user", "{user_question}"),
                    ("system", "{context}")
                ]
            )

            chain = create_stuff_documents_chain(
                llm=self.model,
                prompt=prompt_template
            )

            answer = chain.invoke({
                "user_question": user_question,
                "context": documents,
                "prompt_template": prompt_template,
                "history_message": history_message
            })

            # Store interaction in user-specific memory
            memory.save_context({"input": user_question}, {"output": answer})

            return AnswerEntity(answer)

        except Exception as e:
            raise Exception(f"Error while generating the answer from LangChain model for user {query.get_user_id()}: " + str(e))

    def split_file(self, file: FileEntity) -> list[FileChunkEntity]:
        """
        Given a file entity it split the file in chunks of 10k characters.

        Args:
            file (FileEntity): The file entity to split.

        Returns:
            list[FileChunkEntity]: A list of file chunk entities containing the file chunks.
        """

        # try:
            

        # except Exception as e:
        #     raise Exception("Error while splitting the file: " + str(e))
        