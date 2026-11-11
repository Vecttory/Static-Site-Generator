import re


def extract_markdown_url(regex: str, text: str) -> list[tuple[str, str]]:
    return re.findall(regex, text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return extract_markdown_url(regex, text)


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return extract_markdown_url(regex, text)
