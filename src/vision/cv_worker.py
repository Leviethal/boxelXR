import cv2
import mediapipe as mp
import numpy as np

def cv_loop(camera, hand_tracker, gesture, hand_state):
    mp_draw = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    while True:
        frame = camera.get_frame()
        if frame is None:
            break

        hands = hand_tracker.process(frame)
        if hands:
            for hand in hands:
                started, holding, ended = gesture.detect_pinch(hand.landmark)

                lm = hand.landmark[8]  # index fingertip
                x = (lm.x - 0.5) * 10
                y = -(lm.y - 0.5) * 10
                z = -lm.z * 10

                hand_state.update((x, y, z), holding, frame)

                mp_draw.draw_landmarks(
                    frame, hand, mp_hands.HAND_CONNECTIONS
                )

        # cv2.imshow("BoxelXR CV Debug", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()
