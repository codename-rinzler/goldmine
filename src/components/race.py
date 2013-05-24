class RaceComponent:
    def __init__(self, race, description):
        self.race = race
        self.description = description

        self.name = 'race'

    def __str__(self):
        return self.race
