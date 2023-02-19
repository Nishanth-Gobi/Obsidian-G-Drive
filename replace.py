import os
import re

def path_string(matched_line):    
    match = re.search(r"(.*)!\[(?P<text>[^\]]*)\]\((?P<path>[^)]*)\)(.*)", matched_line)
    if match:
        path = match.group("path")
        return path
    return None


def replace_string_in_file(file_path, search_string, replace_string):
    with open(file_path, 'r') as file:
        content = file.readlines()
    for i, line in enumerate(content):
        if search_string in line:
            print(f"\nline: {line} \nsearch_string: {search_string} \nreplace_string: {replace_string}")
            image_path = path_string(line)
            if image_path:
                content[i] = line.replace(image_path, replace_string)
    with open(file_path, 'w') as file:
        file.writelines(content)


def replace_string_in_directory(directory_path, search_string, replace_string):
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            replace_string_in_directory(item_path, search_string, replace_string)
        elif os.path.isfile(item_path) and item_path.endswith('.md'):
            replace_string_in_file(item_path, search_string, replace_string)
