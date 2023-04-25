class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def alive(self):
        return 0 <= self.x < COUNT_BLOCKS and 0 <= self.y < COUNT_BLOCKS

    def __eq__(self, other):
        return isinstance(other, Player) and self.x == other.x and self.y == other.y
