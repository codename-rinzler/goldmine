import libtcodpy as libtcod

class Tile:
    def __init__(self, blocked, block_sight = None, character = None, bg_color = libtcod.black, fg_color = libtcod.gray, shroud_bg_color = libtcod.Color(50, 50, 150), shroud_fg_color = libtcod.gray):
        self.blocked = blocked;
        self.explored = False
        
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

        self.character = character
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.shroud_bg_color = shroud_bg_color
        self.shroud_fg_color = shroud_fg_color
