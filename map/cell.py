class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.static_entity = None

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"
