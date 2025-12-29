from OpenGL.GL import *

class Cube:
    def __init__(self):
        self.position = (0.0, 0.0, 0.0)

    def set_position(self, pos):
        self.position = pos

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)

        glBegin(GL_QUADS)

        glColor3f(1, 0, 0)
        glVertex3f(1, 1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)

        glColor3f(0, 1, 0)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)

        glEnd()
        glPopMatrix()
