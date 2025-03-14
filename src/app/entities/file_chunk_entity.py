class FileChunkEntity:
    def __init__(self, chunk_content: str, metadata: str):
        self.chunk_content = chunk_content
        self.metadata = metadata

    def get_chunk_content(self) -> str:
        return self.chunk_content
    
    def get_metadata(self) -> str:
        return self.metadata