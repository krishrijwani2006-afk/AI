import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    elif os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    else:
        try:
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
        except Exception as e:
            return f'Error: Could not create directory for file "{file_path}". Exception: {str(e)}'

        with open(target_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'