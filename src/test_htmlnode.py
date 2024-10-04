import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        node2 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        node3= HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        node4 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        node5 = HTMLNode('p', 'pasta', [node, node2, node3, node4], {"href": "https://www.google.com", "target": "_blank",})
        node6 = HTMLNode('p', 'pasta', [node, node2, node3, node4], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_uneq(self):
        node = HTMLNode('p', 'pasta', None, {"href": "https://www.boot.dev", "target": "_blank",})
        node2 = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_print_props(self):
        node = HTMLNode('p', 'pasta', None, {"href": "https://www.google.com", "target": "_blank",})
        line_to_match = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), line_to_match)

    def test_defaults(self):
        node = HTMLNode('p', None, None, None)
        node2 = HTMLNode('p')
        self.assertEqual(node.__repr__(), node2.__repr__())