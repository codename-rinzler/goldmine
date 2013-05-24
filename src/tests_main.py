import unittest
from andromeda import *

class FakeScreen():
    def __init__(self):
        self.fake_data = 6;

class TestThatMainMenuShould(unittest.TestCase):
    
    def setUp(self):
        self.game = AndromedaGame()

    def test_have_one_screen_upon_creation(self):
        self.assertEqual(1, len(self.game.screens))

    def test_have_no_screens_if_popped_after_init(self):
        self.game.pop_screen()
        self.assertEqual(0, len(self.game.screens))

    def test_have_two_screens_if_pushed_after_init(self):
        fake = FakeScreen()
        self.game.push_screen(fake)
        self.assertEqual(2, len(self.game.screens))
        self.assertEqual(fake, self.game.pop_screen())

if __name__ == '__main__':
    unittest.main()
