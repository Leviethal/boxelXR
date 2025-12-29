import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self, config):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=config["max_hands"],
            min_detection_confidence=config["detection_confidence"],
            min_tracking_confidence=config["tracking_confidence"]
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)
        return result.multi_hand_landmarks
