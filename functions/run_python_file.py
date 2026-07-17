import os
import subprocess


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "run a python file in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to the python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "list[string]",
                    "description": "The list of argument to pass to the file to execute, by defaut is set to None",
                },
            },
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    work_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(work_dir, file_path))
    if not os.path.commonpath([target_file, work_dir]) == work_dir :
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(target_file) :
        return (f'Error: "{file_path}" does not exist or is not a regular file')
    if not os.path.exists(target_file):
        return (f'Error: "{file_path}" does not exist or is not a regular file') 
    if not target_file.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file')
    
    command = ["python", target_file]
    if not args == None :
        for each in args:
            command.extend(each)
    
    result = subprocess.run(command, capture_output=True, text=True, timeout=30)
    output_str = ""

    if not result.returncode == 0 :
        output_str += f'Process exited with code {result.returncode}'
    if result.stdout == None and result.stderr == None :
        output_str += f'No output produced'
    output_str += f'STDOUT: {result.stdout}'
    output_str += f'STDERR: {result.stderr}'

    return output_str


