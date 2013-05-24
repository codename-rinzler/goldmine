from race import *
from stats_component import *

class RaceFactory:
    def __init__(self):
        self.races = []
        self.stats = {}
        
        self.races.append(RaceComponent('Gunslinger', 'A shoot first, ask questions later kind of guy.'))
        self.stats['Gunslinger'] = StatsComponent()

        self.races.append(RaceComponent('Gentleman', 'Prefers close combat to shooting from afar. Bar fight specialists.'))
        self.stats['Gentleman'] = StatsComponent(power=7, agility=5, mind=6, speed=4)

        self.races.append(RaceComponent('Hunter', 'A warrior that prefers natural methods of combat. Tracking specialist'))
        self.stats['Hunter'] = StatsComponent(power=4, agility=7, mind=5, speed=7)

        self.races.append(RaceComponent('Shaman', 'A warrior that prefers natural methods of combat. Tracking specialist'))
        self.stats['Shaman'] = StatsComponent(power=2, agility=4, mind=10, speed=5)

    def get_race(self, name):
        found = [race for race in self.races if race.race == name]
        if len(found) > 1:
            raise Exception('RaceFactory.get_race: Found duplicate races')
        if len(found) < 1:
            return None

        return found[0]

    def get_stats_for_race(self, name):
        if name not in self.stats:
            return None
        return self.stats[name]
        
