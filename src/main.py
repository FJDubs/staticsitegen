from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from extractmarkdown import extract_markdown_images, extract_markdown_links
from splitnodes import split_nodes_image, split_nodes_link

def main():
    test = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    #print(test)

    test2 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
    #print(test2.props_to_html())
    #print(test2.__repr__())

    #test3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    #test4 = LeafNode("p", "This is a paragraph of text.")

    #print(test3.to_html())
    #print(test4.to_html())
    '''node1 = ParentNode(
            "p",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )'''

    #print(node1.to_html())

    #print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    #print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
    node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) plus some extra text", 'text')

    split_nodes = split_nodes_image([node])
    for s in split_nodes:
        print(s)

main()