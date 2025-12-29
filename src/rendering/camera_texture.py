import numpy as np
from OpenGL.GL import *

class CameraTexture:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_RGB,
            width,
            height,
            0,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            None
        )

    def update(self, frame):
        frame = frame[:, :, ::-1]  # BGR → RGB
        frame = np.flip(frame, axis=0)  # Flip vertically

        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glTexSubImage2D(
            GL_TEXTURE_2D,
            0,
            0,
            0,
            self.width,
            self.height,
            GL_RGB,
            GL_UNSIGNED_BYTE,
            frame
        )

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
