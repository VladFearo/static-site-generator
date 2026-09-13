from htmlnode import HTMLnode

class LeafNode(HTMLnode):
    def __init__(self, tag: str , value: str , props: dict[str, str] = None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value.strip() == "":
                    raise ValueError("All leaf nodes must have a value.")   
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"