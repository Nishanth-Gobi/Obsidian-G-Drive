import os
import yaml

from drive import get_drive, upload_to_drive
from replace import replace_string_in_directory

# Extract the drive parent id, base path and paths to exclude from the YAML file
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

drive_parent_id = config['drive_parent_id']
base_path = config['base_path']
paths_to_exclude = config['paths_to_exclude']


# get the user's drive
drive = get_drive()


# check if a given file path should be excluded
def is_excluded(file_path, paths_to_exclude):
    for path in paths_to_exclude:
        if file_path.startswith(os.path.join(base_path, path)):
            return True
    return False


upload_file_list = []
image_files = []

# Walk the base directory and list all image files, excluding the specified paths
for dirpath, dirnames, filenames in os.walk(base_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        if not is_excluded(file_path, paths_to_exclude) and os.path.splitext(filename)[1].lower() in ['.jpg', '.jpeg',
                                                                                                      '.png', '.gif']:
            image_files.append(filename)
            upload_file_list.append(file_path)

upload_to_drive(drive=drive, upload_file_list=upload_file_list, parent_id=drive_parent_id)

file_list = drive.ListFile({'q': f"'{drive_parent_id}' in parents and trashed=false"}).GetList()

uploaded_files = {}
for file1 in file_list:
  
#   print('title: %s' % (file1['title']))
  if file1['title'] in image_files:
    #   print('title: %s, id: %s' % (file1['title'], file1['id']))
      uploaded_files[file1['title']] = file1['id']

for key, value in uploaded_files.items():

    replacement_string = 'https://drive.google.com/uc?id=' + value
    replace_string_in_directory(base_path, key, replacement_string)

print("upload file list: ", upload_file_list)
