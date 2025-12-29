import threading

class HandState:
    def __init__(self):
        self.lock = threading.Lock()
        self.smoothed_pos = (0, 0, 0)
        self.pinching = False
        self.frame = None
        self.mask = None

    def update(self, pos, pinching, frame, mask, alpha=0.7):
        with self.lock:
            sx, sy, sz = self.smoothed_pos
            px, py, pz = pos

            self.smoothed_pos = (
                alpha * px + (1 - alpha) * sx,
                alpha * py + (1 - alpha) * sy,
                alpha * pz + (1 - alpha) * sz,
            )

            self.pinching = pinching
            self.frame = frame
            self.mask = mask

    def get(self):
        with self.lock:
            return self.smoothed_pos, self.pinching, self.frame, self.mask
