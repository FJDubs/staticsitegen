import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    textimg = "![alt text](http://example.com/image.png)"
    textealt = "![](http://example.com/image.png)"
    textmi = "![alt one](http://example1.com/image1.png) and ![alt two](http://example2.com/image2.png)"

    textlink = "Here is a [link to Boot.dev](https://www.boot.dev) for you."
    textml = "This text includes [Google](https://www.google.com) and [GitHub](https://github.com) links."
    textnl = "This sentence has no links at all."

    textimagelink = "![alt text](http://example.com/image.png) Here is a [link to Boot.dev](https://www.boot.dev) for you."

    def test_img_output(self):
        expected = [('alt text', 'http://example.com/image.png')]
        self.assertEqual(extract_markdown_images(self.textimg), expected)

    def test_img_empty_alt(self):
        expected = [('', 'http://example.com/image.png')]
        self.assertEqual(extract_markdown_images(self.textealt), expected)

    def test_multi_img(self):
        expected = [('alt one', 'http://example1.com/image1.png'), ('alt two', 'http://example2.com/image2.png')]
        self.assertEqual(extract_markdown_images(self.textmi), expected)
    
    def test_link_output(self):
        expected = [('link to Boot.dev', 'https://www.boot.dev')]
        self.assertEqual(extract_markdown_links(self.textlink), expected)

    def test_multi_link(self):
        expected = [('Google', 'https://www.google.com'), ('GitHub', 'https://github.com')]
        self.assertEqual(extract_markdown_links(self.textml), expected)
    
    def test_no_link(self):
        expected = []
        self.assertEqual(extract_markdown_links(self.textnl), expected)
    def test_both_text(self):
        expected = [[('alt text', 'http://example.com/image.png')], [('link to Boot.dev', 'https://www.boot.dev')]]
        lista = [extract_markdown_images(self.textimagelink), extract_markdown_links(self.textimagelink)]
        self.assertEqual(lista, expected)

if __name__ == "__main__":
    unittest.main()