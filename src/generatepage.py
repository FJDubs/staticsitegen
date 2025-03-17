from markdowntohtmlnode import markdown_to_html_node
from extractmarkdown import extract_title
import re

def genenerate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    from_content = ''
    with open(from_path, 'r') as f:
        from_content = f.read()
    template_content = ''
    with open(template_path, 'r') as f:
        template_content = f.read()
    from_htmlnodes = markdown_to_html_node(from_content)
    content_string = from_htmlnodes.to_html()
    title_string = extract_title(from_content)
    html_page = re.sub(r"{{[\s]*Title[\s]*}}", title_string, template_content)
    html_page = re.sub(r"{{[\s]*Content[\s]*}}", content_string, html_page)
    with open(dest_path, 'w') as f:
        f.write(html_page)