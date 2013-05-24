import unittest
from stats_component import *

class TestThatStatsComponentShould(unittest.TestCase):

    def setUp(self):
        self.stats = StatsComponent()

    def test_initialise_all_values_to_five(self):
        self.assertEqual(5, self.stats.power)
        self.assertEqual(5, self.stats.agility)
        self.assertEqual(5, self.stats.mind)
        self.assertEqual(5, self.stats.speed)

    def test_initialise_all_values_to_params(self):
        self.stats = StatsComponent(power = 2, agility = 4, mind = 6, speed = 8)
        
        self.assertEqual(2, self.stats.power)
        self.assertEqual(4, self.stats.agility)
        self.assertEqual(6, self.stats.mind)
        self.assertEqual(8, self.stats.speed)

if __name__ == '__main__':
    unittest.main()
