import os

DEBUG_MODE = False

def write_file(working_directory, file_path, content):
    try:
        # Ensure we're not getting out of bounds from the working directory
        work_path = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(work_path, file_path))

        if DEBUG_MODE:
            print(f"file_path: {file_path}")
            print(f"work_path: {work_path}")
            print(f"full_path: {full_path}")

        if not full_path.startswith(work_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Ensure full_path directories exist before writing
        leaf_path, leaf_file = os.path.split(full_path)

        if DEBUG_MODE:
            print(f"leaf_path: {leaf_path}")
            print(f"leaf_file: {leaf_file}")
            print(f"exists(leaf_path): {os.path.exists(leaf_path)}")

        if not os.path.exists(leaf_path):
            os.makedirs(leaf_path)
        
            if DEBUG_MODE:
                print(f"makedirs(leaf_path) success: {os.path.exists(leaf_path)}")
        
        with open(full_path, 'w') as f:
            f.write(content) # This will throw IOError if it fails
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"