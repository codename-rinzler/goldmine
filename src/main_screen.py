import libtcodpy as libtcode
from menu import *
from racescreen import *

class MainScreen:
    def __init__(self, parent):
        self.parent = parent
        self.menu = Menu('', ['New Game', 'Quit'], 60, 30, 20, self.parent)

    def render(self):
        self.menu.render()


    def handle_keys(self, key):
        if key == libtcod.KEY_UP:
            self.menu.prev_item()
        elif key == libtcod.KEY_DOWN:
            self.menu.next_item()
        elif key == libtcod.KEY_ENTER:
            item = self.menu.selected_item()
            if item == 'New Game':
                self.parent.push_screen(RaceScreen(self.parent))
            elif item == 'Quit':
                return 'exit'

        return 'turn-taken'
