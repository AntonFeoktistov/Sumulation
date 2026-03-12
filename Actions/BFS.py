from Entities.Creatures import Creature
from Map.Map import Map
from Map.Cell import Cell
from collections import deque


def find_path(creature: Creature, map: Map):
    start = creature.cell
    if is_target_around(creature.cell, map, creature.target):
        return [start]
    queue = deque()
    queue.append((start, [start]))
    visited = []
    visited.append(start)

    while queue:
        current_cell, path = queue.popleft()

        neighbors = get_cells_around(current_cell, map)
        if not neighbors:
            continue
        for neighbor in neighbors:
            # Проверяем, можно ли ступить на клетку
            if not neighbor:
                continue
            if not is_cell_free_to_move(neighbor, map):
                continue
            if neighbor in visited:
                continue
            # Проверим: рядом с neighbor есть цель?
            if is_target_around(neighbor, map, creature.target):
                return path + [neighbor]

            queue.append((neighbor, path + [neighbor]))

    return None


def is_target_around(cell: Cell, map: Map, target: str):
    if cell.x == 0 or cell.x == map.N + 1 or cell.y == 0 or cell.y == map.M + 1:
        return False
    cells_around = get_cells_around(cell, map)
    if not cells_around:
        return False
    for el in cells_around:
        if el in map.field and map.field[el] is not None:  #!!!!
            if target == map.field[el].type:
                return el
    return False


def get_cells_around(cell: Cell, map: Map):
    if cell.x == 0 or cell.y == 0 or (cell.x == map.N + 1) or (cell.y == map.M + 1):
        return []
    up = Cell(cell.x, cell.y - 1)
    down = Cell(cell.x, cell.y + 1)
    left = Cell(cell.x - 1, cell.y)
    right = Cell(cell.x + 1, cell.y)

    return [dir for dir in [up, down, left, right] if dir in map.field]


def is_cell_free_to_move(cell: Cell, map: Map):
    if map.field[cell].type in ("herbivore", "predator", "wall"):
        return False
    return True


def get_dist_between_cells(cell_1: Cell, cell_2: Cell):
    return abs(cell_1.x - cell_2.x) + abs(cell_1.y - cell_2.y)


def find_target_on_map(creature: Creature, map: Map):
    pass
