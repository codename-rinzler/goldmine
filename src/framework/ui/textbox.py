import libtcodpy as libtcod
import textwrap

class TextBox:
    def __init__(self, text, x, y, w, h, parent):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.parent = parent
        self.panel = self.parent.panel
        self.set_text(text)

    def render(self):
        libtcod.console_set_default_background(self.panel, libtcod.black)
        libtcod.console_clear(self.panel)

        y = 1
        for line in self.text:
            libtcod.console_set_default_foreground(self.panel, libtcod.white)
            libtcod.console_print_ex(self.panel, self.x, y+self.y, libtcod.BKGND_NONE, libtcod.LEFT, line)
            y += 1


    def set_text(self, msg):
        self.text = []
        lines = textwrap.wrap(msg, self.width)
        
        for line in lines:
            if len(self.text) == self.height:
                del self.text[0]

            self.text.append(line)
