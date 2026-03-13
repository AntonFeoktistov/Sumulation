from map.map import Map
from map.cell import Cell
from collections import deque


def find_path(creature, map: Map):
    start = creature.cell
    target = creature.target
    if is_target_around(start, map, target):
        return [start]

    queue = deque()
    queue.append((start, [start]))
    visited = {start}

    while queue:
        current_cell, path = queue.popleft()
        neighbors = get_cells_around(current_cell, map)
        for neighbor in neighbors:
            if not is_cell_free_to_move(neighbor, map):
                continue
            if neighbor in visited:
                continue
            if is_target_around(neighbor, map, target):
                return path + [neighbor]

            visited.add(neighbor)  # добавляем в visited сразу
            queue.append((neighbor, path + [neighbor]))

    return None


def is_target_around(cell: Cell, map: Map, target: str):
    if cell.x == 0 or cell.x == map.N + 1 or cell.y == 0 or cell.y == map.M + 1:
        return False
    cells_around = get_cells_around(cell, map)
    for neighbor in cells_around:
        if neighbor in map.field:
            if target == map.get_entity_by_cell(neighbor).type:
                return neighbor
    return False


def get_cells_around(cell: Cell, map: Map):
    if cell.x == 0 or cell.y == 0 or (cell.x == map.N + 1) or (cell.y == map.M + 1):
        return []
    up = map.get_cell_by_coord(cell.x, cell.y - 1)
    down = map.get_cell_by_coord(cell.x, cell.y + 1)
    left = map.get_cell_by_coord(cell.x - 1, cell.y)
    right = map.get_cell_by_coord(cell.x + 1, cell.y)

    return [
        cell
        for cell in [up, right, down, left]
        if cell is not None and cell in map.field
    ]


def is_cell_free_to_move(cell: Cell, map: Map):
    if map.get_entity_by_cell(cell).type in ("herbivore", "predator", "wall"):
        return False
    return True
