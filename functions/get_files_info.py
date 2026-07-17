import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

def get_files_info(working_directory: str, directory: str = ".") -> str:
    work_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(work_dir, directory))
    if not os.path.commonpath([target_dir, work_dir]) == work_dir :
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(target_dir) :
        return (f'Error: "{directory}" is not a directory')


    list = os.listdir(target_dir)
    dic = {}
    string = ""
    for each in list :
        dic[each] = os.path.getsize(target_dir +"/"+ each), os.path.isdir(target_dir +"/"+ each)
        string += "- " + each + ": file_size=" + str(os.path.getsize(target_dir +"/"+ each)) + " bytes, is_dir=" + str(os.path.isdir(target_dir +"/"+ each)) + "\n"
    return string
