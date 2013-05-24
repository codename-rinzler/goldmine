import libtcodpy as libtcod

class StatBar:
    def __init__(self, x, y, width, name, value, maximum, parent, bar_color = libtcod.blue, back_color = libtcod.red):
        self.x = x
        self.y = y
        self.width = width
        self.value = value
        self.maximum = maximum
        self.name = name
        self.parent = parent
        self.bar_color = bar_color
        self.back_color = back_color
        self.panel = self.parent.panel

    def render(self):
        bar_width = int(float(self.value) / self.maximum * self.width)
        
        libtcod.console_set_default_background(self.panel, self.back_color)
        libtcod.console_rect(self.panel, self.x + bar_width, self.y , self.width - bar_width, 1, False, libtcod.BKGND_SCREEN)
 
        libtcod.console_set_default_background(self.panel, self.bar_color)
        if bar_width > 0:
            libtcod.console_rect(self.panel, self.x, self.y, bar_width, 1, False, libtcod.BKGND_SCREEN)

        libtcod.console_set_default_foreground(self.panel, libtcod.white)
        libtcod.console_print_ex(self.panel, self.x + self.width / 2, self.y, libtcod.BKGND_NONE, libtcod.CENTER,
                                 self.name + ': ' + str(self.value) + '/' + str(self.maximum))

    def set_values(self, value, maximum):
        self.value = value
        self.maximum = maximum
