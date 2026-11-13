import unittest

from split_link import split_nodes_with_links
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE,
                         "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_single_image(self):
        node = TextNode(
            "look at the following graph ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("look at the following graph ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_no_image_neither_link(self):
        node = TextNode(
            "look at the following graph",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("look at the following graph", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK,
                         "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_single_link(self):
        node = TextNode(
            "click the next link [link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("click the next link ", TextType.TEXT),
                TextNode("link", TextType.LINK,
                         "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links_and_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)   ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_with_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE,
                         "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK,
                         "https://i.imgur.com/3elNhQu.png"),
                TextNode("   ", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
