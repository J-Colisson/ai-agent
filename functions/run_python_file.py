import os
import subprocess

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


