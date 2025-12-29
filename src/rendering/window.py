import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import *

class GLWindow:
    def __init__(self, width=800, height=600):
        pygame.init()
        pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

        glEnable(GL_DEPTH_TEST)
        gluPerspective(60, width / height, 0.1, 100.0)
        glTranslatef(0.0, 0.0, -10)

    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def swap(self):
        pygame.display.flip()
