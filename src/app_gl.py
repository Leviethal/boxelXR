import threading
import yaml

from camera.webcam_camera import WebcamCamera
from vision.hand_tracker import HandTracker
from vision.gestures import GestureRecognizer
from vision.cv_worker import cv_loop
from interaction.hand_state import HandState

from rendering.window import GLWindow
from rendering.cube import Cube

with open("../config/config.yaml") as f:
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

window = GLWindow()
cube = Cube()

while window.poll_events():
    window.clear()

    pos, pinching = hand_state.get()
    if pinching:
        cube.set_position(pos)

    cube.draw()
    window.swap()
