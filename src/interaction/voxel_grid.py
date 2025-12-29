class VoxelGrid:
    def __init__(self, grid_size=1.0):
        self.grid_size = grid_size
        self.occupied = set()  # stores (x, y, z)

    def snap(self, pos):
        return tuple(
            round(p / self.grid_size) * self.grid_size
            for p in pos
        )

    def is_occupied(self, pos):
        return pos in self.occupied

    def place(self, pos):
        x, y, z = pos
        while (x, y, z) in self.occupied:
            y += self.grid_size
        final = (x, y, z)
        self.occupied.add(final)
        return final