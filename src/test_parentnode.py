import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_tag_raises(self):
        node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_without_children_raises(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_to_html_preserves_child_order(self):
        node = ParentNode("div", [
            LeafNode("b", "first"),
            LeafNode("i", "second"),
            LeafNode("span", "third"),
        ])
        self.assertEqual(
            node.to_html(),
            "<div><b>first</b><i>second</i><span>third</span></div>",
        )

    def test_to_html_with_plain_text_and_nested_children(self):
        node = ParentNode("p", [
            LeafNode(None, "Hello "),
            ParentNode("strong", [LeafNode(None, "world")]),
            LeafNode(None, "!"),
        ])
        self.assertEqual(node.to_html(), "<p>Hello <strong>world</strong>!</p>")

    def test_to_html_with_props(self):
        node = ParentNode("div", [LeafNode("span", "child")], {"class": "container"})
        self.assertEqual(
            node.to_html(),
            '<div class="container"><span>child</span></div>',
        )

    def test_to_html_with_empty_props(self):
        node = ParentNode("div", [LeafNode("span", "child")], {})
        self.assertEqual(node.to_html(), "<div><span>child</span></div>")


if __name__ == "__main__":
    unittest.main()
