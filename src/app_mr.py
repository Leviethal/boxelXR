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
from rendering.mask_texture import MaskTexture
from rendering.draw_hand_depth import draw_hand_depth

from interaction.voxel_grid import VoxelGrid
from interaction.cube_manager import CubeManager

# -------------------------------
# Config
# -------------------------------
with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

# -------------------------------
# CV setup
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
# OpenGL setup
# -------------------------------
window = GLWindow(
    config["camera"]["width"],
    config["camera"]["height"]
)

camera_tex = CameraTexture(
    config["camera"]["width"],
    config["camera"]["height"]
)

mask_tex = MaskTexture(
    config["camera"]["width"],
    config["camera"]["height"]
)

# -------------------------------
# Voxel system
# -------------------------------
voxel_grid = VoxelGrid(grid_size=1.0)
cube_manager = CubeManager(voxel_grid)

# -------------------------------
# Main loop
# -------------------------------
while window.poll_events():
    window.clear()

    pos, pinching, frame, mask = hand_state.get()

    # Background
    if frame is not None:
        camera_tex.update(frame)
        draw_background(camera_tex.texture_id)

    # Hand depth (OCCLUSION)
    if mask is not None:
        mask_tex.update(mask)
        draw_hand_depth(mask_tex.tex_id)

    # Interaction
    if pinching and cube_manager.preview_cube is None:
        cube_manager.start_preview(pos)
    elif pinching:
        cube_manager.update_preview(pos)
    elif not pinching and cube_manager.preview_cube:
        cube_manager.finalize_preview()

    # Render cubes
    for cube in cube_manager.placed_cubes:
        cube.draw()

    if cube_manager.preview_cube:
        cube_manager.preview_cube.draw()

    window.swap()
