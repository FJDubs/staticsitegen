from htmlnode import HTMLNode
from markdowntoblocks import markdown_to_blocks
from blocktoblocktype import block_to_block_type, BlockType
from texttotextnode import text_to_textnode
from parentnode import ParentNode
from leafnode import LeafNode
import re

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = list()
    for block in blocks:
        blocktype = block_to_block_type(block)
        match blocktype:
            case BlockType.HEADING:
                heading_pattern = re.compile(r"^#{1,6}")
                hlen = re.match(heading_pattern, block).span(0)[-1]
                tag = f'h{hlen}'
                value, subnodes = text_to_children(block[hlen:].strip())
                htmlnode = HTMLNode(tag, value, subnodes)
                htmlnodes.append(htmlnode)
            case BlockType.PARAGRAPH:
                value, subnodes = text_to_children(block)
                htmlnode = HTMLNode('p', value, subnodes)
                htmlnodes.append(htmlnode)
            case BlockType.CODE:
                node = ParentNode('pre', LeafNode('code', block[3:-3]))
                htmlnodes.append(node)
            case BlockType.QUOTE:
                cleaned_block = clean_block(block, '> ')
                value, subnodes = text_to_children(cleaned_block)
                htmlnode = HTMLNode('blockquote', value, subnodes)
                htmlnodes.append(htmlnode)
            case BlockType.UNORDEREDLIST:
                cleaned_block = ''
                if block[0] == '*':
                    cleaned_block = clean_block(block, '* ')
                else:
                    cleaned_block = clean_block(block, '- ')
                list_nodes = []
                lines = cleaned_block.split('\n')
                for l in lines:
                    value, subnodes = text_to_children(l)
                    list_nodes.append(HTMLNode('li', value, subnodes))
                htmlnodes.append(ParentNode('ul', list_nodes))
            case BlockType.ORDEREDLIST:
                lines = block.split('\n')
                clean_lines = []
                list_nodes = []
                for l in lines:
                    clean_lines.append(re.sub(r'^\d+\. ', '', l))
                for l in clean_lines:
                    value, subnodes = text_to_children(l)
                    list_nodes.append(HTMLNode('li', value, subnodes))
                htmlnodes.append(ParentNode('ol', list_nodes))
    return ParentNode('div', htmlnodes)


def clean_block(block, remove):
    lines = block.split('\n')
    clean_lines = list()
    for l in lines:
        clean_lines.append(l.strip(remove))
    return '\n'.join(clean_lines)
    

def text_to_children(text):
    nodes = text_to_textnode(text)
    children = []
    for i in range(len(nodes)):
        if i == 0:
            value = nodes[i].text
        else:
            children.append(nodes[i].text_node_to_html_node())
    return value, children