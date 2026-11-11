import unittest

from extract_markdown_url import extract_markdown_links, extract_markdown_images


class TestExtractMarkdownUrl(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_no_matches(self):
        matches = extract_markdown_images(
            "This is text with an ![imaghttpimgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_no_matches(self):
        matches = extract_markdown_links(
            "This is text with an [image(https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [], matches)


if __name__ == "__main__":
    unittest.main()
