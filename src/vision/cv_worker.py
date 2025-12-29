import cv2
import mediapipe as mp
import time
from vision.hand_mask import generate_hand_mask

def cv_loop(camera, hand_tracker, gesture, hand_state):
    mp_hands = mp.solutions.hands

    FPS_LIMIT = 15
    FRAME_TIME = 1.0 / FPS_LIMIT
    last_time = 0.0

    while True:
        now = time.time()
        if now - last_time < FRAME_TIME:
            continue
        last_time = now

        frame = camera.get_frame()
        if frame is None:
            break

        hands = hand_tracker.process(frame)

        # Defaults when no hand is present
        mask = None
        holding = False
        pos = (0.0, 0.0, 0.0)

        if hands:
            mask = generate_hand_mask(
                frame,
                hands,
                frame.shape[1],
                frame.shape[0],
            )

            hand = hands[0]  # single hand
            started, holding, ended = gesture.detect_pinch(hand.landmark)

            lm = hand.landmark[8]  # index fingertip
            x = (lm.x - 0.5) * 10
            y = -(lm.y - 0.5) * 10
            z = -lm.z * 10
            pos = (x, y, z)

        # ALWAYS update hand_state
        hand_state.update(pos, holding, frame, mask)

    camera.release()
