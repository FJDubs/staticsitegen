import unittest
from splitnodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    simple_image = TextNode('Here is an image ![an image](http://image.com) for split_nodes_image.', TextType.TEXT)
    simple_link = TextNode('Here is a link [visit site](http://site.com) for split_nodes_link.', TextType.TEXT)
    multi_image = TextNode('First ![image1](http://image1.com) text then ![image2](http://image2.com) for split_nodes_image.', TextType.TEXT)
    multi_link = TextNode('First [link1](http://link1.com) text then [link2](http://link2.com) for split_nodes_link.', TextType.TEXT)
    link_at_begin_end = TextNode('[Start link](http://start.com) is followed by text and ends with [End link](http://end.com)', TextType.TEXT)
    plain_text = TextNode("Just plain text with no images or links.", TextType.TEXT)

    def test_simple_image(self):
        expected = [TextNode('Here is an image ', TextType.TEXT, None), TextNode('an image', TextType.IMAGE, 'http://image.com'), TextNode(' for split_nodes_image.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_image([self.simple_image]), expected)

    def test_simple_link(self):
        expected = [TextNode('Here is a link ',TextType.TEXT, None), TextNode('visit site', TextType.LINK, 'http://site.com'), TextNode(' for split_nodes_link.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_link([self.simple_link]), expected)

    def test_multi_image(self):
        expected = [TextNode('First ', TextType.TEXT, None), TextNode('image1', TextType.IMAGE, 'http://image1.com'), TextNode(' text then ', TextType.TEXT, None), TextNode('image2', TextType.IMAGE, 'http://image2.com'), TextNode(' for split_nodes_image.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_image([self.multi_image]), expected)

    def test_multi_link(self):
        expected = [TextNode('First ', TextType.TEXT, None), TextNode('link1', TextType.LINK, 'http://link1.com'), TextNode(' text then ', TextType.TEXT, None), TextNode('link2', TextType.LINK, 'http://link2.com'), TextNode(' for split_nodes_link.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_link([self.multi_link]), expected)
    
    def test_link_at_begin_end(self):
        expected = [TextNode('Start link', TextType.LINK, 'http://start.com'), TextNode(' is followed by text and ends with ', TextType.TEXT, None), TextNode('End link', TextType.LINK, 'http://end.com')]
        self.assertEqual(split_nodes_link([self.link_at_begin_end]), expected)
    
    def test_plain_text_image(self):
        expected = [TextNode('Just plain text with no images or links.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_image([self.plain_text]), expected)

    def test_plain_text_link(self):
        expected = [TextNode("Just plain text with no images or links.", TextType.TEXT, None)]
        self.assertEqual(split_nodes_link([self.plain_text]), expected)
    
    def test_multi_input_image(self):
        expected = [TextNode('Here is an image ', TextType.TEXT, None), TextNode('an image', TextType.IMAGE, 'http://image.com'), TextNode(' for split_nodes_image.', TextType.TEXT, None), TextNode('First ', TextType.TEXT, None), TextNode('image1', TextType.IMAGE, 'http://image1.com'), TextNode(' text then ', TextType.TEXT, None), TextNode('image2', TextType.IMAGE, 'http://image2.com'), TextNode(' for split_nodes_image.', TextType.TEXT, None)]
        self.assertEqual(split_nodes_image([self.simple_image, self.multi_image]), expected)

    def test_multi_input_link(self):
        expected = [TextNode('Here is a link ', TextType.TEXT, None), TextNode('visit site', TextType.LINK, 'http://site.com'), TextNode(' for split_nodes_link.', TextType.TEXT, None), TextNode('Start link', TextType.LINK, 'http://start.com'), TextNode(' is followed by text and ends with ', TextType.TEXT, None), TextNode('End link', TextType.LINK, 'http://end.com')]
        self.assertEqual(split_nodes_link([self.simple_link, self.link_at_begin_end]), expected)

if __name__ == "__main__":
    unittest.main()