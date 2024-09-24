import unittest

from textnode import TextNode


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


if __name__ == "__main__":
    unittest.main()