import unittest
from textnode import TextNode
from splitnodesdelimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    node = TextNode("This is text with a `code block` word", 'text')
    new_nodes = split_nodes_delimiter([node], "`", 'code')
    node1 = TextNode("`This` is text with a `code block` word", 'text')
    new_nodes1 = split_nodes_delimiter([node1], "`", 'code')
    nodeb = TextNode("This is text with a **bold** word", "text")
    new_nodesb = split_nodes_delimiter([nodeb], '**', 'bold')
    nodei = TextNode("This is text with a *italic* word", "text")
    new_nodesi = split_nodes_delimiter([nodei], '*', 'italic')
    nodebi = TextNode("This is text with a **bold** and *italic* word", "text")
    new_nodesbi = split_nodes_delimiter([nodebi], '**', 'bold')
    nodeib = TextNode("This is text with a **bold** and *italic* word", "text")
    new_nodesib = split_nodes_delimiter([nodeib], '*', 'italic')

    def test_output_text_first(self):
        self.assertEqual(self.new_nodes, [
            TextNode("This is text with a ", 'text'),
            TextNode("code block", 'code'),
            TextNode(" word", 'text'),
        ])
    
    def test_output_delimiter_first(self):
        self.assertEqual(self.new_nodes1, [
            TextNode("This", 'code'),
            TextNode(" is text with a ", 'text'),
            TextNode("code block", 'code'),
            TextNode(" word", 'text'),
        ])
    
    def test_bold(self):
        self.assertEqual(self.new_nodesb, [
            TextNode("This is text with a ", 'text'),
            TextNode("bold", 'bold'),
            TextNode(" word", 'text'),
        ])

    def test_italic(self):
        self.assertEqual(self.new_nodesi, [
            TextNode("This is text with a ", 'text'),
            TextNode("italic", 'italic'),
            TextNode(" word", 'text'),
        ])
    
    #this only works because ** does not pickup for italics
    def test_bold_with_italic_inside(self):
        self.assertEqual(self.new_nodesbi, [
            TextNode("This is text with a ", 'text'),
            TextNode("bold", 'bold'),
            TextNode(" and *italic* word", 'text'),
        ])
    
    #this should break as multiple inline delimiters are not supported and * picks up bold
    def test_italic_with_bold_inside(self):
        self.assertNotEqual(self.new_nodesbi, [
            TextNode("This is text with a **bold** and ", 'text'),
            TextNode("italic", 'italic'),
            TextNode("word", 'text'),
        ])






if __name__ == "__main__":
    unittest.main()