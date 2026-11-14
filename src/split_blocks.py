from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_blocks(text: str):
    return [
        block.strip()
        for block in text.split("\n\n")
        if block.strip()
    ]


def block_to_block_type(text: str) -> BlockType:
    if re.findall(r"^#{1,6}\s", text):
        return BlockType.HEADING
    if re.findall(r"^`{3}\n[\s\S]*`{3}$", text):
        return BlockType.CODE

    text_lines = text.split("\n")

    if text_lines:
        initial_char = text_lines[0][0]
        if initial_char == '>':
            for line in text_lines:
                if line[0] != '>':
                    break
            return BlockType.QUOTE
        elif initial_char == '-':
            for line in text_lines:
                if line[0] != '-' or line[1] != ' ':
                    break
            return BlockType.UL
        elif initial_char.isdigit():
            for index, line in enumerate(text_lines):
                if not line[0].isdigit() or str(index+1) != line[0] or line[1] != '.':
                    break
            return BlockType.OL

    return BlockType.PARAGRAPH
