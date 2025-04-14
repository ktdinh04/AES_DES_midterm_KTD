import base64

def read_input(file_path):
    """Read input text from a file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().strip()

def write_output(file_path, data):
    """
    Write output data to a file
    Handles both string and bytes data types
    """
    # If data is bytes, convert to base64 string for readable storage
    if isinstance(data, bytes):
        data_str = base64.b64encode(data).decode('utf-8')
    else:
        data_str = str(data)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data_str)

def read_binary(file_path):
    """Read binary data from a file"""
    with open(file_path, 'rb') as file:
        return file.read()

def write_binary(file_path, data):
    """Write binary data to a file"""
    with open(file_path, 'wb') as file:
        file.write(data)