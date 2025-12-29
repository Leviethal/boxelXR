from OpenGL.GL import *

def draw_hand_depth(mask_tex_id):
    # Write depth, not color
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    glDepthMask(GL_TRUE)

    glDisable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, 1, 0, 1, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, mask_tex_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(0, 0, 0)
    glTexCoord2f(1, 0); glVertex3f(1, 0, 0)
    glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
    glTexCoord2f(0, 1); glVertex3f(0, 1, 0)
    glEnd()

    glDisable(GL_TEXTURE_2D)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    # Restore color writes
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glEnable(GL_LIGHTING)
