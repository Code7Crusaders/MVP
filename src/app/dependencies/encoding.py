import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(100000)  
        result = chardet.detect(raw_data)
        return result['encoding']
