from map.cell import Cell


class Map:
    def __init__(self, N=15, M=10):
        self.N = N
        self.M = M
        self.field = {}
        self.cells = {}

    def get_cell_by_coord(self, x: int, y: int):
        return self.cells.get((x, y), None)

    def get_all_creatures(self):
        creatures = []
        for ent in self.field.values():
            if ent.type in ("predator", "herbivore"):
                creatures.append(ent)
        return creatures
