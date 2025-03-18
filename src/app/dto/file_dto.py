class FileDTO:
    def __init__(self, file_name: str, file_content: str):
        self.file_name = file_name
        self.file_content = file_content
    
    def get_file_name(self) -> str:
        return self.file_name

    def get_file_content(self) -> str:
        return self.file_content
