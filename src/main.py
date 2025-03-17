from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from extractmarkdown import extract_markdown_images, extract_markdown_links
from splitnodes import split_nodes_image, split_nodes_link
from texttotextnode import text_to_textnode
from markdowntohtmlnode import markdown_to_html_node
from copydirtopublic import copy_dir_to_public
from generatepage import genenerate_page


def main():
    try:
        copy_dir_to_public('static')
    except ValueError as e:
        print('Error:', e)
    genenerate_page('content/index.md', 'template.html', 'public/index.html')
main()