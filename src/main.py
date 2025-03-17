import os
import shutil
import sys

from copydirtopublic import copy_files_recursive
from generatepage import generate_pages_recursive

basepath = "/"
if sys.argv != "":
    basepath = sys.argv
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


main()