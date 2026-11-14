def markdown_to_blocks(text: str):
    return [
        block.strip()
        for block in text.split("\n\n")
        if block.strip()
    ]
