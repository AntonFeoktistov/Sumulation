from Map.Cell import Cell
from Map.Map import Map


def make_all_move(map: Map):
    creatures = map.get_all_creatures()
    for creature in creatures:
        creature.current_speed = creature.speed
        creature.make_move(map)
        for cell, entity in map.field.items():
            if entity is None:
                raise ValueError(
                    f"Найден None в map.field для клетки {cell} {creature}"
                )
