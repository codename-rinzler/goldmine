import libtcodpy as libtcod
from map import *
from messenger import *
from fov import *

class GameScreen:
    def __init__(self, gamemap, player, parent):
        self.parent = parent
        self.player = None
        self.gamemap = gamemap
        self.player = player
        self.panel = self.parent.panel

        self.color_dark_wall = libtcod.Color(0, 0, 100)
        self.color_light_wall = libtcod.Color(130, 110, 50)
        self.color_dark_ground = libtcod.Color(50, 50, 150)
        self.color_light_ground = libtcod.Color(200, 180, 50)

    def render(self):
        self.gamemap.fov.recompute()

        for x in range(self.gamemap.width):
            for y in range(self.gamemap.height):
                wall = self.gamemap.map[x][y].block_sight
                if not self.gamemap.fov.visible(x, y):
                    if self.gamemap.map[x][y].explored:
                        if wall:
                            libtcod.console_set_char_background(self.panel, x, y, self.color_dark_wall, libtcod.BKGND_SET)
                        else:
                            libtcod.console_set_char_background(self.panel, x, y, self.color_dark_ground, libtcod.BKGND_SET)
                else:
                    if wall:
                        libtcod.console_set_char_background(self.panel, x, y, self.color_light_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_char_background(self.panel, x, y, self.color_light_ground, libtcod.BKGND_SET )
                    self.gamemap.map[x][y].explored = True

        self.player.render(self.panel)
            

    def handle_keys(self, key):
        pos = self.player.components['position']
        if key == libtcod.KEY_ESCAPE:
            #show pause menu
            self.parent.pop_screen()
        elif key == libtcod.KEY_UP:
            pos.up()
            self.gamemap.fov.need_recompute = True
        elif key == libtcod.KEY_DOWN:
            pos.down()
            self.gamemap.fov.need_recompute = True
        elif key == libtcod.KEY_LEFT:
            pos.left()
            self.gamemap.fov.need_recompute = True
        elif key == libtcod.KEY_RIGHT:
            pos.right()
            self.gamemap.fov.need_recompute = True
        return 'turn-taken'
