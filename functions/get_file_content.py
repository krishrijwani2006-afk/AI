import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    else:
        try:
            with open(target_file, "r") as file:
                content = file.read(MAX_CHARS)
                if file.read(1):
                    content += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    
        except Exception as e:
            return f'Error: Could not read file "{file_path}". Exception: {str(e)}'

        else:
            return content

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads the content of a specified file relative to the working directory, returning",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read content from, relative to the working directory"
                }
            }
        }
    }
}
