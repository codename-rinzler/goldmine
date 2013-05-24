import unittest
from race_factory import *

class TestThatRaceFactoryShould(unittest.TestCase):

    def setUp(self):
        self.factory = RaceFactory()

    def test_return_null_if_asked_for_an_unknown_race(self):
        self.assertEqual(None, self.factory.get_race('Unknown'))

    def test_return_null_if_asked_for_stats_of_an_unknown_race(self):
        self.assertEqual(None, self.factory.get_stats_for_race('Unknown'))

    def test_return_right_race_when_invoked(self):
        race = self.factory.get_race('Human')
        self.assertEqual('Human', race.race)

    def test_return_default_stats_for_a_human(self):
        stats = self.factory.get_stats_for_race('Human')
        self.assertEqual(5, stats.power)
        self.assertEqual(5, stats.agility)
        self.assertEqual(5, stats.mind)
        self.assertEqual(5, stats.speed)

    def test_return_correct_stats_for_a_martian(self):
        stats = self.factory.get_stats_for_race('Martian')
        self.assertEqual(3, stats.power)
        self.assertEqual(4, stats.agility)
        self.assertEqual(9, stats.mind)
        self.assertEqual(4, stats.speed)

    def test_return_correct_stats_for_a_zasz(self):
        stats = self.factory.get_stats_for_race('Zasz')
        self.assertEqual(10, stats.power)
        self.assertEqual(2, stats.agility)
        self.assertEqual(4, stats.mind)
        self.assertEqual(3, stats.speed)




        

if __name__ == '__main__':
    unittest.main()
