from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from extractmarkdown import extract_markdown_images, extract_markdown_links
from splitnodes import split_nodes_image, split_nodes_link
from texttotextnode import text_to_textnode

def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    textnode_list = text_to_textnode(text)
    print(textnode_list)

main()