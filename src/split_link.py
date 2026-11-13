from extract_markdown_url import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_with_links(old_nodes: list[TextNode]) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT and node.text:
            nodes.append(node)
            continue

        sub_nodes = []

        images = extract_markdown_images(node.text)
        links = extract_markdown_links(node.text)

        current_text = node.text

        if images:
            for alt_text, url in images:
                separator = f'![{alt_text}]({url})'
                new_texts = current_text.split(separator, 1)
                if new_texts[0]:
                    sub_nodes.append(TextNode(new_texts[0], TextType.TEXT))

                sub_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                current_text = new_texts[1]

            if current_text:
                sub_nodes.append(TextNode(current_text, TextType.TEXT))

            if not links:
                nodes += sub_nodes
                continue

            for sub_node in sub_nodes:
                if sub_node.text_type != TextType.TEXT and sub_node.text:
                    nodes.append(sub_node)
                    continue

                current_text = sub_node.text
                links = extract_markdown_links(current_text)
                for text, url in links:
                    separator = f'[{text}]({url})'
                    new_texts = current_text.split(separator, 1)
                    if new_texts[0]:
                        nodes.append(TextNode(new_texts[0], TextType.TEXT))

                    nodes.append(TextNode(text, TextType.LINK, url))
                    current_text = new_texts[1]

                if current_text:
                    nodes.append(TextNode(current_text, TextType.TEXT))

        elif links:
            for text, url in links:
                separator = f'[{text}]({url})'
                new_texts = current_text.split(separator, 1)
                if new_texts[0]:
                    nodes.append(TextNode(new_texts[0], TextType.TEXT))

                nodes.append(TextNode(text, TextType.LINK, url))
                current_text = new_texts[1]

            if current_text:
                sub_nodes.append(TextNode(current_text, TextType.TEXT))
        elif current_text:
            nodes.append(TextNode(current_text, TextType.TEXT))

    return nodes
