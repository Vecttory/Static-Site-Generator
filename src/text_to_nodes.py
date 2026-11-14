from textnode import TextNode, TextType, TextDelimiter
from split_delimiter import split_nodes_delimiter
from split_link import split_nodes_with_links


def text_to_textnodes(text: str) -> list[TextNode]:
    nodes: list[TextNode] = []
    new_node = TextNode(text, TextType.TEXT)
    nodes.append(new_node)

    nodes = split_nodes_delimiter(
        nodes, TextDelimiter.BOLD.value, TextType.BOLD)

    nodes = split_nodes_delimiter(
        nodes, TextDelimiter.ITALIC.value, TextType.ITALIC)

    nodes = split_nodes_delimiter(
        nodes, TextDelimiter.CODE.value, TextType.CODE)

    nodes = split_nodes_with_links(nodes)

    return nodes
