from Entities import Static_entities

from .Entity import Entity
from Map import Map
from Map.Cell import Cell
from Actions import BFS, turn_actions


class Creature(Entity):
    def __init__(self, cell):
        super().__init__(cell)

    def move_to(self, cell_to: Cell, map: Map):
        if self.cell == cell_to:
            return
        map.field[self.cell] = self.cell.static_entity
        map.field[cell_to] = self
        self.cell = cell_to

    def make_move(self, map: Map):
        path = BFS.find_path(self, map)
        while path:
            self.current_speed += 1
            for cell in path:
                self.move_to(cell, map)
                self.current_speed -= 1
                if self.current_speed == 0:
                    break
            while self.current_speed > 0:
                target_cell = BFS.is_target_around(self.cell, map, self.target)
                if target_cell:
                    self.eat_target(target_cell, map)
                else:
                    break
            path = BFS.find_path(self, map) if self.current_speed > 0 else []

    def eat_target(self, target_cell: Cell, map: Map):
        enemy = map.field[target_cell]
        while self.current_speed > 0 and enemy.hp > 0:
            self.current_speed -= 1
            enemy.hp -= 1
        if enemy.hp <= 0:
            self.kill_enemy(target_cell, map)

    def kill_enemy(self, target_cell: Cell, map: Map):
        self.hp += 2
        if map.field[target_cell].type == "herbiovore":
            map.field[target_cell] = target_cell.static_entity

        if map.field[target_cell].type == "grass":
            map.field[target_cell] = Static_entities.Rock(target_cell)


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
