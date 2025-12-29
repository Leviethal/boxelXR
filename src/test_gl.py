from rendering.window import GLWindow
from rendering.cube import Cube
import time

window = GLWindow()
cube = Cube()

while window.poll_events():
    window.clear()
    cube.draw()
    window.swap()
    time.sleep(0.01)
