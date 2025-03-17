from typing import List
from app.ports.split_file_port import SplitFilePort
from app.models.file_model import FileModel
from app.models.file_chunk_model import FileChunkModel


class SplitFileService:
    def __init__(self, split_file_port: SplitFilePort):
        self.split_file_port = split_file_port

    def split_file(self, file: FileModel) -> List[FileChunkModel]:
        try:
            return self.split_file_port.split_file(file)
        except Exception as e:
            raise e