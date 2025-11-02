import os

MAX_CHARS = 10000

DEBUG_MODE = False

def get_file_content(working_directory, file_path):
    try:
        work_path = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(work_path, file_path))

        if DEBUG_MODE:
            print(f"current working directory: {os.getcwd()}")
            print(f"work_path: {work_path}")
            print(f"full_path: {full_path}")
            print(f"isfile({full_path}): {os.path.isfile(full_path)}")

        if not full_path.startswith(work_path):
            return f'Error: Cannot read "{file_path}" as it is ouside the permitted working directory'
        elif not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if DEBUG_MODE:
            print(f"Number of chars read from {file_path}: {len(file_content_string)}")
        
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            if DEBUG_MODE:
                print(f"file read at: {file_path} was truncated at {MAX_CHARS} characters")
                print("\n")

        return file_content_string
    except Exception as e:
        return f'Error: {e}'
