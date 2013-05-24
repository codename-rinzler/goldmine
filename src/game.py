import libtcodpy as libtcod
from main_screen import *

class AndromedaGame:
    def __init__(self):
        self.screen_width = 80
        self.screen_height = 50
        self.fps = 20

        self.map_width = 80
        self.map_height = 45

        self.panel = libtcod.console_new(self.screen_width, self.screen_height)
        
        self.console = libtcod.console_new(self.map_width, self.map_height)

        self.state = 'main'
        self.main_screen = MainScreen(self)

        self.screens = [self.main_screen]

    def initialise(self):
        libtcod.console_set_custom_font('consolas10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.screen_width, self.screen_height, 'Goldmine', False)
        libtcod.sys_set_fps(self.fps)
        libtcod.console_set_fullscreen(True)

    def run(self):
        while not libtcod.console_is_window_closed():
            self.render()
            libtcod.console_flush()

            key = libtcod.Key()
            mouse = libtcod.Mouse()
            event = libtcod.sys_wait_for_event(1, key, mouse, True)

            if key.vk == libtcod.KEY_ENTER and key.lalt:
                libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())                
            else:
                action = self.screens[-1].handle_keys(key.vk)
                if action == 'exit':
                    return action

    def render(self):
        libtcod.console_set_default_background(0, libtcod.black)
        libtcod.console_set_default_background(self.panel, libtcod.black)
        libtcod.console_clear(0)
        libtcod.console_clear(self.panel)
        self.screens[-1].render()
        libtcod.console_blit(self.panel, 0, 0, self.screen_width, self.screen_height, 0, 0, 0, 1, 1)

    def pop_screen(self):
        return self.screens.pop()

    def push_screen(self, screen):
        self.screens.append(screen)


if __name__ == '__main__':
    game = AndromedaGame()
    game.initialise()
    game.run()
