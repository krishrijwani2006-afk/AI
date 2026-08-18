import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    print(working_dir_abs)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    print(target_dir)
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(target_dir):
        return f'Error: Directory "{directory}" is not a directory'
    else:
        return f'Success: "{directory}" is within the working directory'
        
