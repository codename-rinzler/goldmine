import libtcodpy as libtcod
from rect import Rect
from tile import Tile
from framework.components.position_component import PositionComponent

class Map:
    def __init__(self, width, height, messenger, player):
        self.map = []
        self.gameitems = []
        self.messenger = messenger
        self.player = player
        
        self.reinitialise(width, height)
        

    # setting self.w and self.h here so that we can call this to regen
    # worlds of different sizes without reinit'ing the class
    def reinitialise(self, width, height):
        self.width = width
        self.height = height

        self.map = [[ Tile(True)
                  for y in range(self.height) ]
                    for x in range(self.width) ]


    def create_room(self, room, tile_template = None):
        for x in range(room.x1, room.x2+1):
            for y in range(room.y1, room.y2+1):
                if tile_template:
                    tile = self.map[x][y]
                    tile.blocked = tile_template.blocked
                    tile.block_sight = tile_template.block_sight
                    tile.character = tile_template.character
                    tile.bg_color = tile_template.bg_color
                    tile.fg_color = tile_template.fg_color
                    tile.shroud_bg_color = tile_template.shroud_bg_color
                    tile.shroud_fg_color = tile_template.shroud_fg_color
                else:
                    self.map[x][y].blocked = False
                    self.map[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.map[x][y].blocked:
            return True
 
        for item in self.gameitems:
            if item.blocks and item.x == x and item.y == y:
                return True
 
        return False
