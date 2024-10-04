import unittest
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_defaults(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = HTMLNode("p", "This is a paragraph of text.")
        self.assertEqual(node.__repr__(), node2.__repr__())
    
    def test_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_value_error(self):
        node = LeafNode('p', None)
        with self.assertRaisesRegex(ValueError, "LeafNode must have a value"):
            node.to_html()



#LeafNode("p", "This is a paragraph of text.")
#LeafNode("a", "Click me!", {"href": "https://www.google.com"})