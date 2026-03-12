from Map.Cell import Cell


class Map:
    def __init__(self, N=15, M=10):
        self.N = N
        self.M = M
        self.field = {}

    def get_cell_by_coord(self, x: int, y: int):
        if x < 0 or y < 0 or x > self.N + 1 or y > self.M + 1:
            return None
        for cell in self.field:
            if cell.x == x and cell.y == y:
                return cell
        return None

    def get_all_creatures(self):
        creatures = []
        for ent in self.field.values():
            if ent.type in ("predator", "herbivore"):
                creatures.append(ent)
        return creatures
