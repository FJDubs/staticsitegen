import unittest
from blocktoblocktype import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    one_heading = "# My Heading"
    six_heading = "####### My Heading"
    code_block = "```code\nblock```"
    quote_block = "> This is a quote\n> that spans multiple lines"
    unordered_block = "- Item 1\n- Item 2"
    ordered_block = "1. First\n2. Second\n3. Third"
    paragraph_block = "Just a plain paragraph."
    failed_ordered_block = "- Item 1\n\n- Item 2"

    def test_one_heading(self):
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(self.one_heading), expected)

    def test_six_heading(self):
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(self.six_heading), expected)

    def test_code_block(self):
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(self.code_block), expected)
        
    def test_quote_block(self):
        expected = BlockType.QUOTE
        self.assertEqual(block_to_block_type(self.quote_block), expected)
    
    def test_unordered_block(self):
        expected = BlockType.UNORDEREDLIST
        self.assertEqual(block_to_block_type(self.unordered_block), expected)

    def test_ordered_block(self):
        expected = BlockType.ORDEREDLIST
        self.assertEqual(block_to_block_type(self.ordered_block), expected)

    def test_paragraph_block(self):
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(self.paragraph_block), expected)

    def test_broken_list(self):
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(self.failed_ordered_block), expected)