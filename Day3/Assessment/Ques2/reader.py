"""Create a small Python package with:
1. A module containing a function write_numbers_to_file(filename)
2. The function should write numbers 1–100 into a file
3. Handle possible exceptions such as:
4. Create another module that imports this function and reads the file content safely



File not found

Permission denied"""

from writer import write_numbers_to_file

def read_file_content(filename):
    try:
        with open(filename, "r") as file:
            print("File content:")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found while reading")

    except PermissionError:
        print("Error: Permission denied while reading")


file_name = "numbers.txt"

write_numbers_to_file(file_name)
read_file_content(file_name)