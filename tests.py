from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

# One of the following should be True at a time, others False
TEST_GET_FILES_INFO = False
TEST_GET_FILE_CONTENT = False
TEST_LOREM = False
TEST_WRITE_FILE = False
TEST_RUN_PYTHON_FILE = True

if TEST_GET_FILES_INFO:
    test_cases = [
        ("calculator", "."),
        ("calculator", "pkg"),
        ("calculator", "/bin"),
        ("calculator", "../")
    ]

    for case in test_cases:
        working_directory, directory = case[0], case[1]
        files_info = get_files_info(working_directory, directory)

        if directory == ".":
            directory = "current"
        else:
            directory = f"'{directory}'"

        #print("==============================================")
        print(f"Result for {directory} directory:")
        print(files_info)
        #print("==============================================")
        print("")

if TEST_GET_FILE_CONTENT:
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "pkg/calculator.py"),
        ("calculator", "/bin/cat"),
        ("calculator", "pkg/does_not_exist.py")
    ]

    for case in test_cases:
        working_directory, file_path = case[0], case[1]
        file_content = get_file_content(working_directory, file_path)

        print(f"length of file_content: {len(file_content)}")
        print(f"Contents of file: {file_path}")
        print(file_content)

if TEST_LOREM:
    test_cases = [
        ("calculator", "lorem.txt"),
    ]

    for case in test_cases:
        working_directory, file_path = case[0], case[1]
        file_content = get_file_content(working_directory, file_path)

        print(f"length of file_content: {len(file_content)}")
        print(f"Contents of file: {file_path}")
        print(file_content)

if TEST_WRITE_FILE:
    test_cases = [
        ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
        ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("calculator", "/tmp/tmp.txt", "this should not be allowed"),
    ]

    for case in test_cases:
        working_directory, file_path, content = case
        files_write_status = write_file(working_directory, file_path, content)

        print(files_write_status)

if TEST_RUN_PYTHON_FILE:
    test_cases = [
        ("calculator", "main.py"),
        ("calculator", "main.py", ["3 + 5"]),
        ("calculator", "tests.py"),
        ("calculator", "../main.py"),
        ("calculator", "nonexistent.py"),
        ("calculator", "lorem.txt"),
    ]

    for case in test_cases:
        working_directory, file_path, *args = case
        result = run_python_file(working_directory, file_path, args)

        print(result)