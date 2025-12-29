import threading
import yaml

from src.camera.webcam_camera import WebcamCamera
from src.vision.hand_tracker import HandTracker
from src.vision.gestures import GestureRecognizer
from src.vision.cv_worker import cv_loop
from src.interaction.hand_state import HandState

from src.rendering.window import GLWindow
from src.rendering.cube import Cube
from src.rendering.camera_texture import CameraTexture
from src.rendering.background import draw_background

with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

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

window = GLWindow(
    config["camera"]["width"],
    config["camera"]["height"]
)

cube = Cube()
camera_tex = CameraTexture(
    config["camera"]["width"],
    config["camera"]["height"]
)

while window.poll_events():
    window.clear()

    pos, pinching, frame = hand_state.get()

    if frame is not None:
        camera_tex.update(frame)
        draw_background(camera_tex.texture_id)

    if pinching:
        cube.set_position(pos)

    cube.draw()
    window.swap()
