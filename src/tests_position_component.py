import unittest
from position_component import *

class TestThatPositionComponentShould(unittest.TestCase):
    
    def setUp(self):
        self.pos = PositionComponent(10, 10)

    def test_initialise_with_the_right_values(self):
        self.assertEqual(10, self.pos.x)
        self.assertEqual(10, self.pos.y)

    def test_decrease_y_when_moving_up(self):
        self.pos.up()
        self.assert_position(10, 9)

    def test_increase_y_when_moving_down(self):
        self.pos.down()
        self.assert_position(10, 11)

    def test_decrease_x_when_moving_left(self):
        self.pos.left()
        self.assert_position(9, 10)

    def test_increase_x_when_moving_right(self):
        self.pos.right()
        self.assert_position(11, 10)
        
    def assert_position(self, x, y):
        self.assertEqual(x, self.pos.x)
        self.assertEqual(y, self.pos.y)


if __name__ == '__main__':
    unittest.main()
