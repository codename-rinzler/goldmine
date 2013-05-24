import libtcodpy as libtcod

class GameItem:
    def __init__(self, color = libtcod.white, char = '@'):
        self.components = {}
        self.color = color
        self.char = char

    def add_component(self, component):
        self.components[component.name] = component

    def render(self, panel):
        if 'position' in self.components:
            pos = self.components['position']
            libtcod.console_set_default_foreground(panel, self.color)
            libtcod.console_put_char(panel, pos.x, pos.y, self.char, libtcod.BKGND_NONE)
