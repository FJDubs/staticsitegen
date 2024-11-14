class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_line = ''
        if self.props is not None:
            for p in self.props:
                prop_line += f' {p}="{self.props[p]}"'
        return prop_line
    
    def __repr__(self) -> str:
        return f'[{self.tag}, {self.value}, {self.children}, {self.props}]'
