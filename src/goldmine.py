from framework import game
from main_screen import *

if __name__ == '__main__':
    game = game.RoguelikeGame()
    game.push_screen(MainScreen(game))
    game.initialise()
    game.run()
