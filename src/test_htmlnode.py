import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a normal paragraph",
                        [], {"class": "text"})
        node2 = HTMLNode("p", "This is a normal paragraph",
                         [], {"class": "text"})
        self.assertEqual(str(node), str(node2))

    def test_eq_no_props(self):
        node = HTMLNode("p", "This is a normal paragraph",
                        [])
        node2 = HTMLNode("p", "This is a normal paragraph",
                         [])
        self.assertEqual(str(node), str(node2))

    def test_eq_false(self):
        node = HTMLNode("div", "This is a normal paragraph",
                        [], {"class": "text"})
        node2 = HTMLNode("p", "This is a normal paragraph",
                         [], {"class": "text"})
        self.assertNotEqual(str(node), str(node2))

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Take me there!", {
                        "href": "https://www.boot.dev"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.boot.dev">Take me there!</a>')

    def test_leaf_not_eq_HTMLNode(self):
        node = LeafNode("p", "Hello, world!")
        node2 = HTMLNode("p", "Hello, world!", [], {})
        self.assertNotEqual(str(node), str(node2))


if __name__ == "__main__":
    unittest.main()
