import unittest
from textnode import TextNode, TextType
from texttotextnode import text_to_textnode

class TestTextToTextNode(unittest.TestCase):
    def test_multi_delimiter(self):
        input_text = "This is **bold** and *italic* text."
        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnode(input_text), expected_output)

    def test_link(self):
        input_text = "Click [here](https://www.example.com) for more info."
        expected_output = [
            TextNode("Click ", TextType.TEXT),
            TextNode("here", TextType.LINK, "https://www.example.com"),
            TextNode(" for more info.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnode(input_text), expected_output)

    def test_image(self):
        input_text = "An image: ![alt text](image.jpg) in text."
        expected_output = [
            TextNode("An image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "image.jpg"),
            TextNode(" in text.", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnode(input_text), expected_output)

    def test_combo(self):
        input_text = "**Bold** with `code` and *italic* and ![image](img.png) and [link](https://www.example.com)."
        expected_output = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "img.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.example.com"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnode(input_text), expected_output)





if __name__ == "__main__":
    unittest.main()