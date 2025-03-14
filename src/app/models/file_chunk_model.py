class FileChunkModel:
    def __init__(self, chunk_content: str, metadata: str):
        self._chunk_content = chunk_content
        self._metadata = metadata

    def get_chunk_content(self) -> str:
        return self._chunk_content
    
    def get_metadata(self) -> str:
        return self._metadata
    