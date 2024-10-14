import unittest
from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple(self):
        markdown = "This is a paragraph.\n\nAnd this is another."
        expected = ["This is a paragraph.", "And this is another."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_consecutive_newlines(self):
        markdown = "First block.\n\n\n\nSecond block."
        expected = ["First block.", "Second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_whitespace_only_lines(self):
        markdown = "First block.\n   \n \nSecond block."
        expected = ["First block.", "Second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_leading_ending_whitespace(self):
        markdown = "  First block.  \n\n  Second block.  "
        expected = ["First block.", "Second block."]
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_empty(self):
        markdown = ""
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)

    def test_whitespace_only(self):
        markdown = "   \n \n  \n"
        expected = []
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_complex(self):
        markdown = "# Heading\n\nParagraph here.\n\n* List item 1\n* List item 2\n\nAnother paragraph."
        expected = ["# Heading", "Paragraph here.", "* List item 1\n* List item 2", "Another paragraph."]
        self.assertEqual(markdown_to_blocks(markdown), expected)




if __name__ == "__main__":
    unittest.main()