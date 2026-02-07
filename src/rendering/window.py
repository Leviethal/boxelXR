import pygame
from pygame.locals import DOUBLEBUF, OPENGL, FULLSCREEN
from OpenGL.GL import *
from OpenGL.GLU import *

class GLWindow:
    def __init__(self):
        pygame.init()

        # Get screen resolution
        info = pygame.display.Info()
        width, height = info.current_w, info.current_h

        # Create fullscreen OpenGL window
        pygame.display.set_mode(
            (width, height),
            DOUBLEBUF | OPENGL | FULLSCREEN
        )

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glLightfv(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

        # Correct projection for fullscreen
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, width / height, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10)

    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False  # ESC to exit fullscreen
        return True

    def clear(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    def swap(self):
        pygame.display.flip()
