class FileEntity:
    def __init__(self, filename: str, file_content: str):
        self.filename = filename
        self.file_content = file_content

    def get_filename(self) -> str:
        return self.filename
    
    def get_file_content(self) -> str:
        return self.file_content