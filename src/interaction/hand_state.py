import threading

class HandState:
    def __init__(self):
        self.lock = threading.Lock()
        self.position = (0.0, 0.0, 0.0)
        self.pinching = False
        self.frame = None

    def update(self, pos, pinching, frame):
        with self.lock:
            self.position = pos
            self.pinching = pinching
            self.frame = frame

    def get(self):
        with self.lock:
            return self.position, self.pinching, self.frame
