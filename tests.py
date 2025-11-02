from functions.get_files_info import get_files_info

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