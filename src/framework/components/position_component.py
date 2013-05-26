class PositionComponent:
    def __init__(self, x, y):
        self.name = 'position'
        self.x = x
        self.y = y

    def up(self):
        if self._no_collision(0, -1):
            self.y -= 1

    def down(self):
        if self._no_collision(0, 1):
            self.y += 1

    def left(self):
        if self._no_collision(-1, 0):
            self.x -= 1

    def right(self):
        if self._no_collision(1, 0):
            self.x += 1

    def _no_collision(self, dx, dy):
        if 'mapref' in self.parent.components:
            gamemap = self.parent.components['mapref'].gamemap

            return not gamemap.is_blocked(self.x + dx, self.y + dy)
