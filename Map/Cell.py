class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.entity = None
        self.static_entity = None

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.coord.x}, {self.coord.y})"

    def get_X(self):
        return self._x

    def get_Y(self):
        return self._y

    def set_X(self, x):
        self._x = x

    def set_Y(self, y):
        self._y = y
