import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_without_tag_returns_raw_value(self):
        node = LeafNode(None, "Hello, world!")

        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_preserves_surrounding_whitespace(self):
        node = LeafNode("p", "  Hello, world!  ")

        self.assertEqual(node.to_html(), "<p>  Hello, world!  </p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_props(self):
        node = LeafNode(
            "a",
            "Visit Boot.dev",
            {"href": "https://www.boot.dev", "target": "_blank"},
        )

        self.assertEqual(
            node.to_html(),
            '<a href="https://www.boot.dev" target="_blank">Visit Boot.dev</a>',
        )

    def test_constructor_raises_when_value_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_to_html_raises_when_value_is_empty(self):
        node = LeafNode("p", "")

        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_raises_when_value_is_only_whitespace(self):
        node = LeafNode("p", "   \n\t")

        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode("strong", "Important", {"class": "warning"})

        self.assertEqual(
            repr(node),
            "LeafNode(strong, Important, {'class': 'warning'})",
        )


if __name__ == "__main__":
    unittest.main()
