class PositionComponent:
    def __init__(self, x, y):
        self.name = 'position'
        self.x = x
        self.y = y

    def up(self):
        self.y -= 1

    def down(self):
        self.y += 1

    def left(self):
        self.x -= 1

    def right(self):
        self.x += 1
