from framework.map import *
from framework.fov import *

class SaloonGenerator:
    def __init__(self):
        pass

    def generate_top_floor(self, player):
        gamemap = Map(28, 12, None, None)
        for r in range(5):
            room = Rect(3+(r*5), 1, 3, 3)
            gamemap.create_room(room)

        gamemap.create_room(Rect(1, 1, 0, 5))
        gamemap.create_room(Rect(1, 6, 25, 0))
        gamemap.create_room(Rect(1, 8, 25, 2))
        
        for x in range(5):
            gamemap.create_room(Rect(6+(x*5), 5, 0, 0))

        gamemap.create_room(Rect(13, 7, 3, 0))
        
        fov = FieldOfView(player, gamemap, gamemap.width, gamemap.height)
        fov.recompute()
        gamemap.fov = fov

        return gamemap
        

    
