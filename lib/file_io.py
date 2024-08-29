"""
Plan

1. Define the write_file function:
    - Add .txt extension to file_name.
    - Open the file in write mode and write file_content to it.
2. Define the append_file function:
    - Add .txt extension to file_name.
    - Open the file in append mode and append append_content to it.
3. Define the read_file function:
    - Add .txt extension to file_name.
    - Open the file in read mode and return its content.
"""

def write_file(file_name, file_content):
    file_name = f"{file_name}.txt"
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name = f"{file_name}.txt"
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    file_name = f"{file_name}.txt"
    with open(file_name, 'r') as file:
        return file.read()

        
