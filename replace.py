import os

def replace_string_in_file(file_path, search_string, replace_string):
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace(search_string, replace_string)
    with open(file_path, 'w') as file:
        file.write(content)

def replace_string_in_directory(directory_path, search_string, replace_string):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            replace_string_in_directory(item_path, search_string, replace_string)
        elif os.path.isfile(item_path) and item_path.endswith('.md'):
            replace_string_in_file(item_path, search_string, replace_string)
            print(f"Replaced '{search_string}' with '{replace_string}' in file: {item_path}")
