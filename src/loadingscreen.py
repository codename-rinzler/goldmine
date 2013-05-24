import libtcodpy as libtcod
from textbox import *
from map import *
from messenger import *
from fov import *
from gamescreen import *

class LoadingScreen:
    def __init__(self, parent):
        self.parent = parent
        self.textbox = TextBox('Generating world...', 3, 42, 74, 1, self.parent)
        self.player = None
        self.gamemap = None

    def render(self):
        self.textbox.render()

    def handle_keys(self, key):
        if not self.gamemap:
            self._do_mapgen()
        else:
            self.parent.pop_screen()
            self.parent.push_screen(GameScreen(self.gamemap, self.player, self.parent))
    
        return 'turn-taken'

    def _do_mapgen(self):
        self.gamemap = Map(40, 40, Messenger(4, 40), self.player)
        self.gamemap.make_map()
        fov = FieldOfView(self.player, self.gamemap, self.gamemap.width, self.gamemap.height)
        fov.recompute()
        self.gamemap.fov = fov

        self.textbox.set_text('Done. Press any key to continue...')

        


        
