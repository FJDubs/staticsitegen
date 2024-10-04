from textnode import TextNode
from htmlnode import HTMLNode

def main():
    test = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(test)

    test2 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
    print(test2.props_to_html())
    print(test2.__repr__())

main()