import time

from Map.Map import Map
from Map.Cell import Cell
from Renderer.Renderer import Renderer
from Actions import BFS, init_actions, turn_actions

map = Map(15, 10)
init_actions.initialize_map(map)
Renderer.to_render(map)
creatures = map.get_all_creatures()
for cr in creatures:
    old_cell = cr.cell
    cr.make_move(map)
    print(cr.cell.static_entity)
    print(cr.type, old_cell, "сделал ход на ", cr.cell)
    for cell in map.field:
        # print(cell.static_entity)
        if map.field[cell] is None:
            print(cell, " ")

Renderer.to_render(map)
"""for cr in creatures:
    path = BFS.find_path(cr, map)
    print(cr.type, " ", end="")
    for cell in path:
        print(cell, end=" ")"""
"""for el in map.field.keys():
    print(el, ":", str(BFS.get_cells_around(el, map)))"""

"""creatures = map.get_all_creatures()
for cr in creatures:
    print(cr.type, " ", cr.cell)
    cr.make_move(map)"""
"""while True:
    Renderer.to_render(map)
    turn_actions.make_all_move(map)
    time.sleep(2)"""
