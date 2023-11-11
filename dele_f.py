import os

def delete_files(directory_path):
    for filename in os.listdir(directory_path):
            if os.path.isfile(os.path.join(directory_path, filename)):
                os.remove(os.path.join(directory_path, filename))

def file_del():
    delete_files('static/files/output')
    delete_files('static/files/output/format_video')
    delete_files('static/files/output/video')