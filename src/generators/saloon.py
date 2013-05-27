from framework.map import *
from framework.fov import *

class SaloonGenerator:
    def __init__(self):
        self.generate_tile_templates()

    def generate_top_floor(self, player):
        gamemap = Map(28, 12, None, None)

        gamemap.create_room(Rect(0, 0, 27, 7), self.saloon_wall)
        gamemap.create_room(Rect(0, 8, 27, 3), self.wooden_pickets)

        for r in range(5):
            room = Rect(3+(r*5), 1, 3, 3)
            gamemap.create_room(room, self.carpet_floor)

        gamemap.create_room(Rect(1, 1, 0, 5), self.carpet_floor)
        gamemap.create_room(Rect(1, 6, 25, 0), self.carpet_floor)
        gamemap.create_room(Rect(1, 8, 25, 2), self.wooden_slats)
        
        for x in range(5):
            gamemap.create_room(Rect(6+(x*5), 5, 0, 0), self.carpet_floor)

        gamemap.create_room(Rect(12, 7, 5, 0), self.wooden_slats)
        
        fov = FieldOfView(player, gamemap, gamemap.width, gamemap.height)
        fov.recompute()
        gamemap.fov = fov

        return gamemap
        

    def generate_tile_templates(self):
        self.carpet_floor = Tile(False, False,'.', libtcod.light_red, libtcod.white)
        self.wooden_slats = Tile(False, False,'=', libtcod.Color(180, 160, 45), libtcod.Color(130, 110, 50))
        self.wooden_pickets = Tile(True, False,'#', libtcod.Color(180, 160, 45), libtcod.Color(130, 110, 50))
        self.saloon_wall = Tile(True, True, None, libtcod.Color(130, 110, 50), libtcod.white, libtcod.Color(0, 0, 100))
