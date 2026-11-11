import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextType, TextNode


class TestTextNode(unittest.TestCase):
    def test_empty_node_list(self):
        nodes = split_nodes_delimiter([], "*", TextType.BOLD)
        self.assertEqual(nodes, [])

    def test_missing_closing_delimiter(self):
        with self.assertRaises(ValueError):
            split_nodes_delimiter(
                [
                    TextNode("This is a **text node", TextType.TEXT)
                ], "**", TextType.BOLD)

    def test_multiple_node_types(self):
        nodes = split_nodes_delimiter(
            [
                TextNode("This is a _text italic node_ **xx bold xx**",
                         TextType.TEXT),
                TextNode("This is a bold node", TextType.BOLD),
                TextNode("This is an _italic node_", TextType.TEXT)
            ], "_", TextType.ITALIC)

        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

        self.assertEqual(len(nodes), 7)
        self.assertEqual(nodes[0], TextNode("This is a ", TextType.TEXT))
        self.assertEqual(nodes[1], TextNode(
            "text italic node", TextType.ITALIC))
        self.assertEqual(nodes[2], TextNode(" ", TextType.TEXT))
        self.assertEqual(nodes[3], TextNode("xx bold xx", TextType.BOLD))
        self.assertEqual(nodes[4], TextNode(
            "This is a bold node", TextType.BOLD))
        self.assertEqual(nodes[5], TextNode("This is an ", TextType.TEXT))
        self.assertEqual(nodes[6], TextNode("italic node", TextType.ITALIC))

    def test_not_appending_empty_value_nodes(self):
        nodes = split_nodes_delimiter(
            [
                TextNode("", TextType.TEXT),
                TextNode("", TextType.ITALIC),
                TextNode("", TextType.BOLD),
                TextNode("", TextType.CODE),
            ], "_", TextType.ITALIC)

        self.assertEqual(len(nodes), 0)


if __name__ == "__main__":
    unittest.main()
