import libtcodpy as libtcode
from menu import *
from textbox import *
from role import *
from role_factory import *
from gameitem import *
from loadingscreen import *

class RoleScreen:
    def __init__(self, parent):
        self.parent = parent
        self.textbox = TextBox('', 3, 42, 74, 5, self.parent)
        self.player = None

        self.factory = RoleFactory()
        self.menu = Menu('', self.factory.roles, 3, 3, 15, self.parent)

    def render(self):
        current = self.menu.selected_item()
        self.textbox.set_text(current.description)

        self.textbox.render()
        self.menu.render()

    def handle_keys(self):
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.menu.prev_item()
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.menu.next_item()
        elif libtcod.console_is_key_pressed(libtcod.KEY_ENTER):
            if self.player:
                stats = self.menu.selected_item()
                self.player.add_component(stats)
                
            self.parent.pop_screen()
            self.parent.pop_screen()
            
            loadingscreen = LoadingScreen(self.parent)
            loadingscreen.player = self.player
            self.parent.push_screen(loadingscreen)


        return 'turn-taken'
