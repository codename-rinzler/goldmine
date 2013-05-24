import libtcodpy as libtcode
from framework.gameitem import GameItem
from framework.ui.menu import Menu
from framework.ui.textbox import TextBox
from framework.ui.statbar import StatBar
from race import *
from race_factory import *
from loadingscreen import *

class RaceScreen:
    def __init__(self, parent):
        self.parent = parent
        self.textbox = TextBox('', 3, 42, 74, 5, self.parent)

        self.factory = RaceFactory()
        self.menu = Menu('', self.factory.races, 3, 3, 15, self.parent)

        self.power_bar = StatBar(57, 4, 20, 'Power', 7, 10, self.parent, libtcod.dark_red, libtcod.gray)
        self.agility_bar = StatBar(57, 7, 20, 'Agility', 4, 10, self.parent, libtcod.darker_sea, libtcod.gray)
        self.mind_bar = StatBar(57, 10, 20, 'Mind', 5, 10, self.parent, libtcod.orange, libtcod.gray)
        self.speed_bar = StatBar(57, 13, 20, 'Speed', 5, 10, self.parent, libtcod.light_blue, libtcod.gray)

    def render(self):
        current = self.menu.selected_item()
        self.textbox.set_text(current.description)
        stats = self.factory.get_stats_for_race(current.race)
        self.power_bar.set_values(stats.power, 10)
        self.agility_bar.set_values(stats.agility, 10)
        self.mind_bar.set_values(stats.mind, 10)
        self.speed_bar.set_values(stats.speed, 10)

        self.textbox.render()
        self.power_bar.render()
        self.agility_bar.render()
        self.mind_bar.render()
        self.speed_bar.render()
        self.menu.render()

    def handle_keys(self, key):
        if key == libtcod.KEY_ESCAPE:
            self.parent.pop_screen()
        elif key == libtcod.KEY_UP:
            self.menu.prev_item()
        elif key == libtcod.KEY_DOWN:
            self.menu.next_item()
        elif key == libtcod.KEY_ENTER:
            player = GameItem()
            race = self.menu.selected_item()
            stats = self.factory.get_stats_for_race(race.race)
            player.add_component(race)
            player.add_component(stats)
            
            loadingscreen = LoadingScreen(self.parent)
            loadingscreen.player = player
            self.parent.pop_screen()
            self.parent.push_screen(loadingscreen)


        return 'turn-taken'
