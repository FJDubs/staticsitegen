from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode must have a tag')
        if self.children is None:
            raise ValueError('ParentNode must have children nodes')
        html_line = f'<{self.tag}>'
        for c in self.children:
            html_line += c.to_html()
        return html_line + f'</{self.tag}>'
