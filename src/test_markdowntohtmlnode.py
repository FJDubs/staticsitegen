import unittest
from markdowntohtmlnode import markdown_to_html_node
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_headers(self):
        test = '# Heading1\n\n## Heading2'
        expected = ParentNode('div', [HTMLNode('h1', 'Heading1', [], None), HTMLNode('h2', 'Heading2', [], None)], None)
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())
    
    def test_paragraph(self):
        test = '#Wrong Header\n\nJust some plain text\n\nA multi\nline'
        expected = ParentNode('div', [HTMLNode('p', '#Wrong Header', [], None), HTMLNode('p', 'Just some plain text', [], None), HTMLNode('p', 'A multi\nline', [], None)], None)
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_code_block(self):
        test = '```Code block```'
        expected = ParentNode('div', [ParentNode('pre', LeafNode('code', 'Code block'))])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_quote(self):
        test = '> A multi-line quote.\n> About code so strange but\n> Really a haiku'
        expected = ParentNode('div', [HTMLNode('blockquote', 'A multi-line quote.\nAbout code so strange but\nReally a haiku', [])])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())
    
    def test_unordered_list(self):
        test = '* Item 1\n* Item 2\n* Item 3'
        expected = ParentNode('div', [(ParentNode('ul', [HTMLNode('li', 'Item 1', []), HTMLNode('li', 'Item 2', []), HTMLNode('li', 'Item 3', [])]))])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())
    
    def test_ordered_list(self):
        test = '1. Item 1\n2. Item 2\n3. Item 3'
        expected = ParentNode('div', [(ParentNode('ol', [HTMLNode('li', 'Item 1', []), HTMLNode('li', 'Item 2', []), HTMLNode('li', 'Item 3', [])]))])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_in_line_node(self):
        test = 'A paragraph with **BOLD**'
        expected = ParentNode('div', [HTMLNode('p', 'A paragraph with ', [LeafNode('b', 'BOLD')])])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_empty(self):
        test = ''
        expected = ParentNode('div', [])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_empty_multiline(self):
        test = '\n\n\n\n\n\n'
        expected = ParentNode('div', [])
        self.assertEqual(markdown_to_html_node(test).__repr__(), expected.__repr__())

    def test_whitespace(self):
        assert markdown_to_html_node("   \n   \n").to_html()



if __name__ == "__main__":
    unittest.main()