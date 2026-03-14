import random

from map.map import Map
from map.cell import Cell
from entities import creatures, static_entities
from entities.static_entities import Wall

GRASS_CHANCE = 50
TREE_CHANCE = 30
CREATURE_CHANCE = 10
HERBIVORE_CHANCE = 70  # процент от всех животных на карте


def initialize_map(map: Map):
    for i in range(map.M + 2):
        for j in range(map.N + 2):
            cell = Cell(j, i)
            map.cells[(j, i)] = cell
            if i == 0 or j == 0 or (i == map.M + 1) or (j == map.N + 1):
                wall = Wall(cell)
                map.set_entity_to_cell(cell, wall)
                cell.static_entity = wall
                wall.cell = cell
            else:
                static_entity = make_random_static_entity(cell)
                map.set_entity_to_cell(cell, static_entity)
                cell.static_entity = static_entity
                number = random.randint(1, 100)
                if number <= CREATURE_CHANCE:
                    creature = make_random_creature(cell)
                    map.set_entity_to_cell(cell, creature)
                    creature.cell = cell
                else:
                    cell.entity = cell.static_entity
                    static_entity.cell = cell


def make_random_static_entity(cell: Cell):
    number = random.randint(1, 100)
    if number < GRASS_CHANCE:
        return static_entities.Grass(cell)
    if GRASS_CHANCE <= number <= GRASS_CHANCE + TREE_CHANCE:
        return static_entities.Tree(cell)
    return static_entities.Rock(cell)


def make_wall(cell: Cell):
    return static_entities.Wall(cell)


def make_random_creature(cell: Cell):
    number = random.randint(1, 100)
    if number <= HERBIVORE_CHANCE:
        return creatures.Herbivore(cell)
    return creatures.Predator(cell)
