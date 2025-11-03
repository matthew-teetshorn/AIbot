import os
import subprocess

DEBUG_MODE = False

def run_python_file(working_directory, file_path, args=[]):
    try:
        # Ensure we're not getting out of bounds from the working directory
        work_path = os.path.abspath(working_directory)
        full_path = os.path.abspath(os.path.join(work_path, file_path))

        if DEBUG_MODE:   
            print(f"file_path: {file_path}")
            print(f"work_path: {work_path}")
            print(f"full_path: {full_path}")
            arg_string = ""
            for arg in args:
                arg_string += (f" {arg}")
            print(f"args: {arg_string}")
            
        if not full_path.startswith(work_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        
        root, extension = os.path.splitext(file_path)
        if extension != ".py":
            return f'Error: "{file_path}" is not a Python file.'
        
    except Exception as e:
        return f"Error: {e}"
    
    try:
        # Run the provided file
        cmd = ["python", full_path]
        for arg in args:
            cmd += arg

        if DEBUG_MODE:
            print(f"cmd: {cmd}")

        completed_process = subprocess.run(args=cmd,
                                           capture_output=True,
                                           text=True,
                                           timeout=30,
                                           cwd=working_directory)
        
        output = completed_process.stdout
        error = completed_process.stderr
        ret_code = completed_process.returncode

        if DEBUG_MODE:
            print(f"stdout: {completed_process.stdout}")
            print(f"stderr: {completed_process.stderr}")

        ret_str = ""
        if output == error == None:
            return "No output produced."
        if output:
            ret_str += f"STDOUT: {output} "
        if error:
            ret_str += f"STDERR: {error}"
        if completed_process.returncode != 0:
            ret_str = f"Process exited with code {ret_code} "
        
        ret_str.rstrip()
        return ret_str
    except Exception as e:
        return f"Error: executing Python file: {e}"