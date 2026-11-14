import unittest

from split_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestSplitBlocks(unittest.TestCase):
    def test_eq(self):

        text = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""

        blocks = markdown_to_blocks(text)
        expected_blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]

        self.assertEqual(blocks, expected_blocks)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockToBlockType(unittest.TestCase):
    def test_eq_headings(self):
        results = []
        for i in range(0, 8):
            results.append(block_to_block_type(
                f'{'#' * i} This is a heading {1}'))
        expected_results = [BlockType.PARAGRAPH] + \
            [BlockType.HEADING] * 6 + [BlockType.PARAGRAPH]
        self.assertEqual(results, expected_results)

    def test_eq_code(self):
        text = "```\nThis should be recognized as a code block\ncd ..\nstart run dev\nthe server has started\n```"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.CODE)

    def test_eq_quote(self):
        text = ">hello\n>\n> I am a quote\n>\n>\n>\nThis is another quote\n>"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_eq_unordered_list(self):
        text = "- this is 1\n- this is 2  \n- This is Three\n- "
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.UL)

    def test_eq_ordered_list(self):
        text = "1. this is 1\n2. this is 2  \n3. This is Three"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.OL)

    def test_eq_paragraph(self):
        text = "This should be a normal paragraph\nGoodbye"
        block_type = block_to_block_type(text)
        self.assertEqual(block_type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
