import unittest
from textbox import *

class FakeParent():
    def __init__(self):
        self.panel = None
        self.screen_height = 100

class TestThatTextBoxShould(unittest.TestCase):

    def test_be_initialised_correctly(self):
        parent = FakeParent()
        textbox = TextBox("this is my text", 5, 5, 30, 7, parent)

        self.assertEqual("this is my text", textbox.text[0])
        self.assertEqual(5, textbox.x)
        self.assertEqual(5, textbox.y)
        self.assertEqual(30, textbox.width)
        self.assertEqual(7, textbox.height)
        self.assertEqual(parent, textbox.parent)

if __name__ == '__main__':
    unittest.main()
