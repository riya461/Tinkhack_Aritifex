import os
import os

def delete_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".md") or filename.endswith(".gif"):
            pass
        else:
            if os.path.isfile(os.path.join(directory_path, filename)):
                os.remove(os.path.join(directory_path, filename))