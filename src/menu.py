import libtcodpy as libtcod

class Menu:
    def __init__(self, header, options, x, y, width, parent, text_color = libtcod.white, selected_bkgnd = libtcod.red, unselected_bkgnd = libtcod.black):
        self.header = header
        self.parent = parent
        self.options = options
        self.selected_index = 0
        self.x = x
        self.y = y
        self.width = width
        self.header_height = libtcod.console_get_height_rect(self.parent.panel, 0, 0, self.width, self.parent.screen_height, header)
        self.height = len(self.options) + self.header_height
        self.panel = self.parent.panel
        self.text_color = text_color
        self.selected_bkgnd = selected_bkgnd
        self.unselected_bkgnd = unselected_bkgnd
 
    def render(self):
        libtcod.console_set_default_foreground(self.panel, self.text_color)
        libtcod.console_print_rect_ex(self.panel, self.x, self.y, self.width, self.height, libtcod.BKGND_NONE, libtcod.LEFT, self.header)

        y = self.header_height
        for option_text in self.options:
            if (option_text == self.options[self.selected_index]):
                libtcod.console_set_default_background(self.panel, self.selected_bkgnd)
            else:
                libtcod.console_set_default_background(self.panel, self.unselected_bkgnd)

            libtcod.console_print_ex(self.panel, self.x, y + self.y, libtcod.BKGND_SET, libtcod.LEFT, str(option_text))
            y += 1

    def next_item(self):
        self.selected_index += 1
        if self.selected_index >= len(self.options):
            self.selected_index = 0

    def prev_item(self):
        self.selected_index -= 1
        if self.selected_index < 0:
            self.selected_index = len(self.options) - 1

    def selected_item(self):
        return self.options[self.selected_index]
