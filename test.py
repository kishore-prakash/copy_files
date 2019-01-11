import os
import shutil
import json

with open('selected_1.json') as file:
        data = json.load(file)

folders = data["folders"]
# print(folders)
for folder in folders:
        src = folder["src"]
        dest = folder["dest"]
        if not os.path.exists(dest):
                os.makedirs(dest)
        src_files = folder["files"]
        print(src_files)
        for file_name in src_files:
                src_full_path = os.path.join(src, file_name)
                dest_fill_path = os.path.join(dest, file_name)
                if (os.path.isfile(src_full_path)):
                        shutil.copy(src_full_path, dest_fill_path)
