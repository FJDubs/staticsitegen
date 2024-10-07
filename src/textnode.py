from leafnode import LeafNode
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textnode):
        if (self.text == textnode.text and
            self.text_type == textnode.text_type and
            self.url == textnode.url):
            return True
        return False
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'
    
    def text_node_to_html_node(self):
        match self.text_type:
            case 'text':
                return LeafNode(None, self.text)
            case 'bold':
                return LeafNode('b', self.text)
            case 'italic':
                return LeafNode('i', self.text)
            case 'code':
                return LeafNode('code', self.text)
            case 'link':
                return LeafNode('a', self.text, {'href': self.url})
            case 'image':
                return LeafNode('img', '', {'src': self.url, 'alt': self.text})
            case _:
                raise ValueError('Text type is not supported')
