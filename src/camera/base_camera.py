class BaseCamera:
    def get_frame(self):
        raise NotImplementedError

    def release(self):
        pass
