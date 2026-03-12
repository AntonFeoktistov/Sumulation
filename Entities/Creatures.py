from .Entity import Entity
from Map import Map


class Creature(Entity):
    def __init__(self, cell):
        super().__init__(cell)

    def make_move(self, field: Map):
        pass


class Predator(Creature):
    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 4
        self.current_speed = 4
        self.hp = 10
        self.type = "predator"
        self.target = "herbivore"


class Herbivore(Creature):

    def __init__(self, cell):
        super().__init__(cell)
        self.speed = 4
        self.current_speed = 4
        self.hp = 10
        self.type = "herbivore"
        self.target = "grass"
