from os import path, listdir, mkdir
from shutil import copy, rmtree

def copy_dir_to_public(dir):
    if not path.exists(dir):
        raise ValueError(f'{dir} directory does not exist.\nPlease include and update {dir} directory')
    if path.exists('public'):
        rmtree('public')
    mkdir('public')
    get_files(dir, "public")
    
def get_files(dir, dest):
    dir_list = listdir(dir)
    for item in dir_list:
        item_path = path.join(dir, item)
        dest_path = path.join(dest, item)
        print(f'Looking at: {item_path}')
        if not item[0] == '.' and path.isdir(item_path):
            mkdir(dest_path)
            print(f'Entering: {item_path}')
            get_files(item_path, dest_path)
        elif not item[0] == '.' and path.isfile(item_path):
            print(f'Copying: {item_path}')
            copy(item_path, dest)