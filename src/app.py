import cv2
import yaml
from camera.webcam_camera import WebcamCamera
from vision.hand_tracker import HandTracker
from vision.gestures import GestureRecognizer
import mediapipe as mp

with open("../config/config.yaml") as f:
    config = yaml.safe_load(f)

camera = WebcamCamera(
    config["camera"]["index"],
    config["camera"]["width"],
    config["camera"]["height"]
)

hand_tracker = HandTracker(config["hand_tracking"])
gesture = GestureRecognizer(config["gestures"]["pinch_threshold"])

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

while True:
    frame = camera.get_frame()
    if frame is None:
        break

    hands = hand_tracker.process(frame)
    if hands:
        for hand in hands:
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            started, holding, ended = gesture.detect_pinch(hand.landmark)
            if started:
                print("PINCH START")
            if ended:
                print("PINCH END")

    cv2.imshow("BoxelXR - Hand Debug", frame)

    # VERY IMPORTANT
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

camera.release()
cv2.destroyAllWindows()
