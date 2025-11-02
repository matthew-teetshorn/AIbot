from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# One of the following should be True at a time, others False
TEST_GET_FILES_INFO = False
TEST_GET_FILE_CONTENT = True
TEST_LOREM = False

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
