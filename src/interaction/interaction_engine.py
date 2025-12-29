class InteractionEngine:
    def __init__(self, voxel_grid):
        self.voxel_grid = voxel_grid
        self.active_cube = None

    def on_pinch_start(self, position):
        snapped = self.voxel_grid.place(position)
        self.active_cube = snapped

    def on_pinch_move(self, position):
        if self.active_cube:
            self.active_cube = self.voxel_grid.snap(position)

    def on_pinch_end(self):
        self.active_cube = None
