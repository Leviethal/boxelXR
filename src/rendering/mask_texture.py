import numpy as np
from OpenGL.GL import *

class MaskTexture:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.tex_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glTexImage2D(
            GL_TEXTURE_2D,
            0,
            GL_LUMINANCE,
            width,
            height,
            0,
            GL_LUMINANCE,
            GL_UNSIGNED_BYTE,
            None
        )

    def update(self, mask):
        glBindTexture(GL_TEXTURE_2D, self.tex_id)
        glTexSubImage2D(
            GL_TEXTURE_2D,
            0,
            0,
            0,
            self.width,
            self.height,
            GL_LUMINANCE,
            GL_UNSIGNED_BYTE,
            mask
        )
