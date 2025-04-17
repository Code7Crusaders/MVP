from models.file_chunk_model import FileChunkModel
from ports.add_chunks_port import AddChunksPort

class AddChunksService:

    def __init__(self, add_chunks_port: AddChunksPort ):
        self.add_chunks_port = add_chunks_port


    def load_chunks(self, chunks: list[FileChunkModel]):
        try:
            self.add_chunks_port.load_chunks(chunks)        
        except Exception as e:
            raise e 
        