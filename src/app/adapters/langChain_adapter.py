from app.models.answer_model import AnswerModel
from app.models.context_model import ContextModel
from app.models.question_model import QuestionModel
from app.models.file_chunk_model import FileChunkModel
from app.models.file_model import FileModel
from app.models.prompt_template_model import PromptTemplateModel

from app.entities.query_entity import QueryEntity
from app.entities.document_context_entity import DocumentContextEntity
from app.entities.file_entity import FileEntity

from app.repositories.langChain_repository import LangChainRepository
from app.ports.split_file_port import SplitFilePort
from app.ports.generate_answer_port import GenerateAnswerPort

class LangChainAdapter(GenerateAnswerPort, SplitFilePort):
    
    def __init__(self, lang_chain_repository: LangChainRepository):
        self.lang_chain_repository = lang_chain_repository

    def generate_answer(self, question: QuestionModel, context: list[ContextModel], prompt_template: PromptTemplateModel) -> AnswerModel:
        # Implement the logic to generate an answer using the lang_chain_repository

        question_entity = QueryEntity(question.get_user_id(), question.get_question())

        context_entities = []
        for context_model in context:
            context_entities.append( DocumentContextEntity(context_model.get_content()) )

        answer = self.lang_chain_repository.generate_answer(question_entity, context_entities, prompt_template.get_prompt_template_content())

        return AnswerModel(answer.get_answer())

    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        # Implement the logic to split the file into chunks using the lang_chain_repository

        file_entity = FileEntity(file.get_filename(), file.get_file_content())

        file_chunks = self.lang_chain_repository.split_file(file_entity)

        file_chunk_models = []
        for file_chunk in file_chunks:
            file_chunk_models.append( FileChunkModel( file_chunk.get_chunk_content(), file_chunk.get_metadata()) )

        return file_chunk_models

