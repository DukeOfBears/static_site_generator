import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.mail()