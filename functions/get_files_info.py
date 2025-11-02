import os

DEBUG_MODE = False

def get_files_info(working_directory, directory="."):
    working_directory_abs_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory_abs_path, directory))
    
    if DEBUG_MODE:
        print(f"working_directory: {working_directory}")
        print(f"directory: {directory}")
        print(f"full_path: {full_path}")
        print(f"working_directory_abs_path: {working_directory_abs_path}")
        print(f"current working directory: {os.getcwd()}")
        

    if not (full_path == working_directory_abs_path or
            full_path.startswith(working_directory_abs_path + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        contents = os.listdir(full_path)
        ret_str = ""

        if DEBUG_MODE:
            print(f"listdir contents: {contents}")

        for item in contents:
            child_path = os.path.join(full_path, item)
            size = os.path.getsize(child_path)
            is_dir = os.path.isdir(child_path)

            if DEBUG_MODE:
                print(f"contents item: {item}")
                print(f"child_path: {child_path}")
                print(f"size: {size}")
                print(f"is_dir: {is_dir}")

            ret_str += f"- {item}: file_size={size} bytes, is_dir={is_dir}\n"
        return ret_str
    except Exception as e:
        return f"Error: {e}"




# os.path.abspath(): Get an absolute path from a relative path
# os.path.join(): Join two paths together safely (handles slashes)
# .startswith(): Check if a string starts with a substring
# os.path.isdir(): Check if a path is a directory
# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
