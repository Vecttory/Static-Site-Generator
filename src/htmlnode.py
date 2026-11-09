class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] = [], props: dict[str, str] = {}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "to_html method must be implemented in subclasses")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        props_str = " ".join(f'{key}="{value}"' for key,
                             value in self.props.items())
        return f" {props_str}"

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={len(self.children)}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = {}):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("All parent nodes must have a tag.")
        if not self.children:
            print(self.children)
            raise ValueError("All parent nodes must have children.")
        return f'<{self.tag}>{"".join(child.to_html() for child in self.children)}</{self.tag}>'


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict[str, str] = {}):
        super().__init__(tag=tag, value=value, children=[], props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"
