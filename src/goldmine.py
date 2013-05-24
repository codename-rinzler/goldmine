from framework.game import RoguelikeGame
from screens.main_screen import MainScreen

if __name__ == '__main__':
    game = RoguelikeGame()
    game.push_screen(MainScreen(game))
    game.initialise()
    game.run()
