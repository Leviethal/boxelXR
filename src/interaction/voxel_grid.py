class VoxelGrid:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.occupied = set()

    def snap(self, pos):
        return tuple(round(p / self.grid_size) * self.grid_size for p in pos)

    def place(self, pos):
        snapped = self.snap(pos)
        self.occupied.add(snapped)
        return snapped
