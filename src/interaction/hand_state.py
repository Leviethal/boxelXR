import threading

class HandState:
    def __init__(self):
        self.lock = threading.Lock()
        self.position = (0.0, 0.0, 0.0)
        self.pinching = False

    def update(self, pos, pinching):
        with self.lock:
            self.position = pos
            self.pinching = pinching

    def get(self):
        with self.lock:
            return self.position, self.pinching
