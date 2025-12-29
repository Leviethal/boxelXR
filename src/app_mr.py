import threading
import yaml

from camera.webcam_camera import WebcamCamera
from vision.hand_tracker import HandTracker
from vision.gestures import GestureRecognizer
from vision.cv_worker import cv_loop
from interaction.hand_state import HandState

from rendering.window import GLWindow
from rendering.camera_texture import CameraTexture
from rendering.background import draw_background

from interaction.voxel_grid import VoxelGrid
from interaction.cube_manager import CubeManager

# -------------------------------
# Load config
# -------------------------------
with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

# -------------------------------
# Camera + CV setup
# -------------------------------
camera = WebcamCamera(
    config["camera"]["index"],
    config["camera"]["width"],
    config["camera"]["height"]
)

hand_tracker = HandTracker(config["hand_tracking"])
gesture = GestureRecognizer(config["gestures"]["pinch_threshold"])

hand_state = HandState()

cv_thread = threading.Thread(
    target=cv_loop,
    args=(camera, hand_tracker, gesture, hand_state),
    daemon=True
)
cv_thread.start()

# -------------------------------
# OpenGL / MR setup
# -------------------------------
window = GLWindow(
    config["camera"]["width"],
    config["camera"]["height"]
)

camera_tex = CameraTexture(
    config["camera"]["width"],
    config["camera"]["height"]
)

# -------------------------------
# Voxel system (FEATURE A)
# -------------------------------
voxel_grid = VoxelGrid(grid_size=1.0)
cube_manager = CubeManager(voxel_grid)

# -------------------------------
# Main render loop
# -------------------------------
while window.poll_events():
    window.clear()

    pos, pinching, frame = hand_state.get()

    # Draw camera background
    if frame is not None:
        camera_tex.update(frame)
        draw_background(camera_tex.texture_id)

    # -------- Interaction Logic --------
    if pinching and cube_manager.preview_cube is None:
        cube_manager.start_preview(pos)

    elif pinching:
        cube_manager.update_preview(pos)

    elif not pinching and cube_manager.preview_cube:
        cube_manager.finalize_preview()

    # -------- Render Cubes --------
    for cube in cube_manager.placed_cubes:
        cube.draw()

    if cube_manager.preview_cube:
        cube_manager.preview_cube.draw()

    window.swap()
