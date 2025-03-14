from app.models.answer_model import AnswerModel
from app.models.context_model import ContextModel
from app.models.question_model import QuestionModel
from app.models.file_chunk_model import FileChunkModel
from app.models.file_model import FileModel

from app.repositories.langChain_repository import LangChainRepository
from app.ports.split_file_port import SplitFilePort

class LangChainAdapter(SplitFilePort):
    
    def __init__(self, lang_chain_repository: LangChainRepository):
        self.lang_chain_repository = lang_chain_repository

    def generate_answer(self, question: QuestionModel, context: list[ContextModel]) -> AnswerModel:
        # Implement the logic to generate an answer using the lang_chain_repository
        pass

    def split_file(self, file: FileModel) -> list[FileChunkModel]:
        # Implement the logic to split the file into chunks using the lang_chain_repository
        pass