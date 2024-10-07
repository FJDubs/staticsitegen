import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
    node1 = ParentNode(
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
        )
    node2 = ParentNode('p', None)
    node3 = ParentNode(None, LeafNode("b", "Bold text"))
    def test_to_html(self):
        self.assertEqual(self.node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_nested_parent(self):
        self.assertEqual(self.node1.to_html(), '<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>Normal text<i>italic text</i>Normal text</p>')
    def test_no_childern_err(self):
        with self.assertRaisesRegex(ValueError, 'ParentNode must have children nodes'):
            self.node2.to_html()
    def test_no_tag_err(self):
        with self.assertRaisesRegex(ValueError, 'ParentNode must have a tag'):
            self.node3.to_html()
    