from extract_markdown_url import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT and node.text:
            nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        links = extract_markdown_links(node.text)

        if images and links:
            raise ValueError(
                "Cannot have both images and links in the same text node")

        current_text = node.text
        index = 0

        while current_text:
            if not images and not links:
                nodes.append(TextNode(current_text, TextType.TEXT))
                break

            if images:
                match = images[index]  # tuple[alt text, url]
                match_type = TextType.IMAGE
            else:
                match = links[index]  # tuple[str, url]
                match_type = TextType.LINK

            separator = f'{'!' if match_type == TextType.IMAGE else ''}[{match[0]}]({match[1]})'
            print(separator)

            new_texts = current_text.split(separator, 1)
            index += 1
            print(new_texts)

            current_text = new_texts[1]

            if new_texts[0]:
                nodes.append(TextNode(new_texts[0], TextType.TEXT))

            nodes.append(TextNode(match[0], match_type, match[1]))

    return nodes
