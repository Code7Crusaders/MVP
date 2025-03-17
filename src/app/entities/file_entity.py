class FileEntity:
    def __init__(self, metadata: str, file_content: str):
        self.metadata = metadata
        self.file_content = file_content

    def get_metadata(self) -> str:
        return self.metadata
    
    def get_file_content(self) -> str:
        return self.file_content