import random

from Map.Map import Map
from Map.Cell import Cell
from Entities import Creatures, Static_entities
from Entities.Static_entities import Wall


def initialize_map(map: Map):
    for i in range(map.M + 2):
        for j in range(map.N + 2):
            cell = Cell(j, i)
            if i == 0 or j == 0 or (i == map.M + 1) or (j == map.N + 1):
                wall = Wall(cell)
                map.field[cell] = wall
                cell.static_entity = wall
                wall.cell = cell
            else:
                static_entity = make_random_static_entity(cell)
                map.field[cell] = static_entity
                cell.static_entity = static_entity
                number = random.randint(1, 100)
                if number <= 20:
                    creature = make_random_creature(cell)
                    map.field[cell] = creature
                    creature.cell = cell
                else:
                    cell.entity = cell.static_entity
                    static_entity.cell = cell


def make_random_static_entity(cell: Cell):
    number = random.randint(1, 100)
    if number < 60:
        return Static_entities.Grass(cell)
    if 60 <= number <= 80:
        return Static_entities.Tree(cell)
    return Static_entities.Rock(cell)


def make_wall(cell: Cell):
    return Static_entities.Wall(cell)


def make_random_creature(cell: Cell):
    number = random.randint(1, 100)
    if number <= 50:
        return Creatures.Herbivore(cell)
    return Creatures.Predator(cell)
