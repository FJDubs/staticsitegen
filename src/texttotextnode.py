from splitnodes import split_nodes_image, split_nodes_link
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_textnode(text):
    textnodes = [TextNode(text, TextType.TEXT)]
    
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    textnodes = split_nodes_delimiter(textnodes, '**', TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, '_', TextType.ITALIC)
    textnodes = split_nodes_image(textnodes)
    textnodes = split_nodes_link(textnodes)
    
    return textnodes
