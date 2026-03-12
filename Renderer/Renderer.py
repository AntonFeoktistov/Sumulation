from Map.Map import Map
from Map.Cell import Cell


class Renderer:
    sprites = {
        "grass": "🍀",
        "rock": "🗻",
        "tree": "🌲",
        "wall": "🧱",
        "predator": "🦊",
        "herbivore": "🐐",
    }

    def to_render(map: Map):
        for i in range(map.M + 2):
            for j in range(map.N + 2):
                cell = Cell(j, i)
                type = map.field[cell].type
                print(
                    Renderer.sprites[type],
                    end="",
                )
            print()
