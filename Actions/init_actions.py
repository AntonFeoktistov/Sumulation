import random

from map.map import Map
from map.cell import Cell
from entities import creatures, static_entities
from entities.static_entities import Wall


def initialize_map(map: Map):
    for i in range(map.M + 2):
        for j in range(map.N + 2):
            cell = Cell(j, i)
            map.cells[(j, i)] = cell
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
                if number <= 15:
                    creature = make_random_creature(cell)
                    map.field[cell] = creature
                    creature.cell = cell
                else:
                    cell.entity = cell.static_entity
                    static_entity.cell = cell


def make_random_static_entity(cell: Cell):
    number = random.randint(1, 100)
    if number < 50:
        return static_entities.Grass(cell)
    if 50 <= number <= 80:
        return static_entities.Tree(cell)
    return static_entities.Rock(cell)


def make_wall(cell: Cell):
    return static_entities.Wall(cell)


def make_random_creature(cell: Cell):
    number = random.randint(1, 100)
    if number <= 75:
        return creatures.Herbivore(cell)
    return creatures.Predator(cell)
