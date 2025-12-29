from rendering.cube import Cube

class CubeManager:
    def __init__(self, voxel_grid):
        self.voxel_grid = voxel_grid
        self.placed_cubes = []
        self.preview_cube = None

    def start_preview(self, pos):
        snapped = self.voxel_grid.snap(pos)
        self.preview_cube = Cube(snapped)

    def update_preview(self, pos):
        if self.preview_cube:
            snapped = self.voxel_grid.snap(pos)
            self.preview_cube.set_position(snapped)

    def finalize_preview(self):
        if self.preview_cube:
            pos = self.preview_cube.position

            final_pos = self.voxel_grid.place(pos)
            self.preview_cube.set_position(final_pos)
            self.placed_cubes.append(self.preview_cube)

            self.preview_cube = None
