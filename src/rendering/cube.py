from OpenGL.GL import *

class Cube:
    def __init__(self):
        self.position = (0, 0, 0)

    def set_position(self, pos):
        self.position = pos

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)

        glBegin(GL_QUADS)

        # FRONT
        glNormal3f(0, 0, 1)
        glColor3f(0.6, 0.8, 1.0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)

        # BACK
        glNormal3f(0, 0, -1)
        glColor3f(0.4, 0.6, 0.9)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)

        # LEFT
        glNormal3f(-1, 0, 0)
        glColor3f(0.3, 0.5, 0.8)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)

        # RIGHT
        glNormal3f(1, 0, 0)
        glColor3f(0.5, 0.7, 0.9)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)

        # TOP
        glNormal3f(0, 1, 0)
        glColor3f(0.7, 0.9, 1.0)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)

        # BOTTOM
        glNormal3f(0, -1, 0)
        glColor3f(0.2, 0.4, 0.6)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)

        glEnd()
        glPopMatrix()
