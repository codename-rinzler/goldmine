import unittest
from gameitem import *

class FakeComponent():
    def __init__(self):
        self.name = 'fake'
        self.fake_data = 6;

class TestThatGameItemShould(unittest.TestCase):
    
    def setUp(self):
        self.item = GameItem()

    def test_contain_no_components_when_created(self):
        self.assertEqual(0, len(self.item.components))

    def test_contain_one_named_component_when_added_to(self):
        fake = FakeComponent()
        self.item.add_component(fake)
        self.assertEqual(1, len(self.item.components))
        self.assertTrue(fake.name in self.item.components)
        self.assertEqual(fake.name, self.item.components[fake.name].name)
        self.assertEqual(fake.fake_data, self.item.components[fake.name].fake_data)

if __name__ == '__main__':
    unittest.main()
