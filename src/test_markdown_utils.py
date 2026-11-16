import unittest

from markdown_utils import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_get_h1(self):
        md = """
# this is my title

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        title = extract_title(md)
        self.assertEqual(title, "this is my title")

    def test_get_h1_not_in_first_line(self):
        md = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items

# this is my title 1

This is a line of text

# this is my title 2

"""

        title = extract_title(md)
        self.assertEqual(title, "this is my title 1")

    def test_no_title_found(self):
        md = """
this is a not well formatted title

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        with self.assertRaises(ValueError) as context:
            extract_title(md)

        self.assertEqual(str(context.exception),
                         "Markdown missing a title (eg. '# My title')")
