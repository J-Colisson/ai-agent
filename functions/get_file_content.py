import os

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Give the content of a file in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to get the content of the file, relative to the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    work_dir = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(work_dir, file_path))
    if not os.path.commonpath([target_file, work_dir]) == work_dir :
        return (f'Error: Cannot list "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(target_file) :
        return (f'Error: File not found or is not a regular file : "{file_path}"')
    if not os.path.exists(target_file) :
        return (f'Error: File not found or is not a regular file : "{file_path}"')

    MAX_CHARS = 10000
    with open(target_file) as f:
        string = str(f.read(MAX_CHARS))

        if not f.read(1) == "":
            string += f'[...File "{file_path}" truncated at {MAX_CHARS}]'
    return string