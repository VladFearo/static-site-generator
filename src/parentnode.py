from htmlnode import HTMLnode

class ParentNode(HTMLnode):
     def __init__(self, tag: str, children: list["HTMLnode"], props: dict[str, str] = None):
        super().__init__(tag, None, children, props)


     def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required for ParentNode")
        if self.children is None:
            raise ValueError("Children are required for ParentNode")
        props_html = f" {self.props_to_html()}" if self.props else ""
        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>" 