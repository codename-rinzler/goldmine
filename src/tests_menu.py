import unittest
from menu import *

class FakeParent():
    def __init__(self):
        self.panel = None
        self.screen_height = 100

class FakeObject():
    def __init__(self):
        self.fake_data = 101

class TestThatMenuShould(unittest.TestCase):

    def setUp(self):
        self.menu = Menu('Test', ['A', 'B', 'C'], 0, 0, 100, FakeParent())

    def test_initially_select_the_first_item(self):
        self.assertEqual('A', self.menu.selected_item())

    def test_return_the_second_item_after_next_item_is_called(self):
        self.menu.next_item()

        self.assertEqual('B', self.menu.selected_item())

    def test_wrap_forward(self):
        self.menu.next_item()
        self.menu.next_item()
        self.menu.next_item()

        self.assertEqual('A', self.menu.selected_item())

    def test_return_the_first_item_if_next_is_called_followed_by_prev(self):
        self.menu.next_item()
        self.menu.prev_item()

        self.assertEqual('A', self.menu.selected_item())

    def test_wrap_backwards(self):
        self.menu.prev_item()

        self.assertEqual('C', self.menu.selected_item())

    def test_returns_selected_object(self):
        self.menu.options = [FakeObject()]

        self.assertTrue(self.menu.selected_item() is not None)
        self.assertEqual(101, self.menu.selected_item().fake_data)

if __name__ == '__main__':
    unittest.main()
