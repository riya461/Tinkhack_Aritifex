import os
def delete_files(path):
    for root, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                pass
            else:
                os.remove(os.path.join(root, file))