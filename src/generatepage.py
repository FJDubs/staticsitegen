from markdowntohtmlnode import markdown_to_html_node
from extractmarkdown import extract_title
import re
import os

def generate_page(dir_path_content, template_path, dest_dir_path, basepath):
    print(f'Generating page from {dir_path_content} to {dest_dir_path} using {template_path}')
    from_content = ''
    with open(dir_path_content, 'r') as f:
        from_content = f.read()
    template_content = ''
    with open(template_path, 'r') as f:
        template_content = f.read()
    from_htmlnodes = markdown_to_html_node(from_content)
    content_string = from_htmlnodes.to_html()
    title_string = extract_title(from_content)
    html_page = re.sub(r"{{[\s]*Title[\s]*}}", title_string, template_content)
    html_page = re.sub(r"{{[\s]*Content[\s]*}}", content_string, html_page)
    html_page = re.sub(r'href="/', f'href="{basepath}', html_page)
    html_page = re.sub(r'src="/', f'src="{basepath}', html_page)
    with open(dest_dir_path, 'w') as f:
        f.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isdir(from_path):
            
            dest_subdir = os.path.join(dest_dir_path, filename)
            generate_pages_recursive(from_path, template_path, dest_subdir, basepath)
        elif filename.endswith('.md'): 
            dest_filename = filename[:-3] + '.html'  
            dest_path = os.path.join(dest_dir_path, dest_filename)
            print(f" * {from_path} -> {dest_path}")
            generate_page(from_path, template_path, dest_path, basepath)
    

