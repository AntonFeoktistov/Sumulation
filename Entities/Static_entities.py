from .entity import Entity


class Grass(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.hp = 13
        self.type = "grass"


class Rock(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.type = "rock"


class Tree(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.type = "tree"


class Wall(Entity):
    def __init__(self, cell):
        super().__init__(cell)
        self.type = "wall"
