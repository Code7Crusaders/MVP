from models.answer_model import AnswerModel
from models.context_model import ContextModel
from models.question_model import QuestionModel
from models.file_chunk_model import FileChunkModel
from models.file_model import FileModel
from models.prompt_template_model import PromptTemplateModel

from entities.query_entity import QueryEntity
from entities.document_context_entity import DocumentContextEntity
from entities.file_entity import FileEntity

from repositories.langChain_repository import LangChainRepository
from ports.split_file_port import SplitFilePort
from ports.generate_answer_port import GenerateAnswerPort

class LangChainAdapter(GenerateAnswerPort, SplitFilePort):
    
    def __init__(self, lang_chain_repository: LangChainRepository):
        self.lang_chain_repository = lang_chain_repository

    def generate_answer(self, question: QuestionModel, context: list[ContextModel], prompt_template: PromptTemplateModel) -> AnswerModel:
        """
        Generates an answer based on the given question, context, and prompt template.

        Args:
            question (QuestionModel): The question model containing the user ID and question text.
            context (list[ContextModel]): A list of context models containing the context content.
            prompt_template (PromptTemplateModel): The prompt template model containing the prompt template content.

        Returns:
            AnswerModel: The generated answer model containing the answer text.
        """
        question_entity = QueryEntity(question.get_user_id(), question.get_question())

        context_entities = []
        for context_model in context:
            context_entities.append(DocumentContextEntity(context_model.get_content()))

        answer = self.lang_chain_repository.generate_answer(question_entity, context_entities, prompt_template.get_prompt_template_content())

        return AnswerModel(answer.get_answer())

    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        """
        Splits the given file into chunks.

        Args:
            file (FileModel): The file model containing the filename and file content.

        Returns:
            list[FileChunkModel]: A list of file chunk models containing the chunk content and metadata.
        """
        file_entity = FileEntity(file.get_filename(), file.get_file_content())

        file_chunks = self.lang_chain_repository.split_file(file_entity)

        file_chunk_models = []
        for file_chunk in file_chunks:
            file_chunk_models.append(FileChunkModel(file_chunk.get_chunk_content(), file_chunk.get_metadata()))

        return file_chunk_models

