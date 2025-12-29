import numpy as np

class GestureRecognizer:
    def __init__(self, threshold):
        self.threshold = threshold
        self.is_pinching = False

    def detect_pinch(self, landmarks):
        thumb = np.array([landmarks[4].x, landmarks[4].y])
        index = np.array([landmarks[8].x, landmarks[8].y])
        dist = np.linalg.norm(thumb - index)

        pinch_now = dist < self.threshold
        started = pinch_now and not self.is_pinching
        ended = not pinch_now and self.is_pinching

        self.is_pinching = pinch_now
        return started, pinch_now, ended
