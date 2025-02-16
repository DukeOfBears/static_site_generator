import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is another text node", TextType.CODE, "https://boot.dev")
        node2 = TextNode("This is another text node", TextType.CODE, "https://boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is first text node", TextType.CODE, "https://boot.dev")
        node2 = TextNode("This is second text node", TextType.CODE, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("Same text here", TextType.LINK)
        node2 = TextNode("Same text here", TextType.IMAGE)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("Some random stuff", TextType.ITALIC, "https://boot.dev")
        node = TextNode("Some random stuff", TextType.ITALIC, "https://google.com")

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.mail()
