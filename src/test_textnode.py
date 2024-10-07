import unittest

from textnode import TextNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode('TextNode1', 'bold')
        node2 = TextNode('TextNode2', 'bold')
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode('TextNode1', 'bold', None)
        node2 = TextNode('TextNode1', 'bold')
        self.assertEqual(node, node2)

    def test_print(self):
        node = TextNode('TextNode1', 'bold', 'https://github.com/FJDubs')
        self.assertEqual('TextNode(TextNode1, bold, https://github.com/FJDubs)', repr(node))
    
    def test_text_to_leaf(self):
        node = TextNode('this is text', 'text')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode(None, 'this is text').__repr__())

    def test_bold_to_leaf(self):
        node = TextNode('this is bold', 'bold')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode('b', 'this is bold').__repr__())

    def test_italic_to_leaf(self):
        node = TextNode('this is italic', 'italic')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode('i', 'this is italic').__repr__())

    def test_code_to_leaf(self):
        node = TextNode('this is code', 'code')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode('code', 'this is code').__repr__())

    def test_link_to_leaf(self):
        node = TextNode('this is a link', 'link', 'boot.dev')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode('a', 'this is a link', {'href': 'boot.dev'}).__repr__())

    def test_img_to_leaf(self):
        node = TextNode('this is an image', 'image', 'boot.dev')
        self.assertEqual(node.text_node_to_html_node().__repr__(), LeafNode('img', '', {'src': 'boot.dev', 'alt': 'this is an image'}).__repr__())

    def test_unsuported(self):
        node = TextNode('this should error', 'error')
        with self.assertRaisesRegex(ValueError, 'Text type is not supported'):
            node.text_node_to_html_node()

if __name__ == "__main__":
    unittest.main()