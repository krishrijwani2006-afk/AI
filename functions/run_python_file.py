import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if not valid_target_file:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    elif '.py' not in file_path:
        return f'Error: "{file_path}" is not a Python file'
    else:
        try:
            command = ["python", target_file]
            if args:
                command.extend(args)
            process = subprocess.run(command, capture_output=True, text=True, timeout=30)
            
        except Exception as e:
            return f"Error: executing Python file: {e}"
        else:
            if process.returncode != 0:
                return process.stdout + f'\nProcess exited with code {process.returncode}'
            elif not process.stdout and not process.stderr:
                return process.stdout + f'\nNo output produced'
            else:
                return f'STDOUT: {process.stdout}\nSTDERR: {process.stderr}'


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file relative to the working directory, with optional command-line arguments, and returns the output or error messages",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the Python file to execute, relative to the working directory"
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional command-line arguments to pass to the Python file"
                }
            }
        }
    }
}