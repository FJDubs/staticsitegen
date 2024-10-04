from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    test = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    #print(test)

    test2 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
    #print(test2.props_to_html())
    #print(test2.__repr__())

    test3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    test4 = LeafNode("p", "This is a paragraph of text.")

    print(test3.to_html())
    print(test4.to_html())

main()