import pyglet
import images
from spaceship import Spaceship


window_width = 1000
window_height = 600


objects = []
keys = set()
window = pyglet.window.Window(
    window_width, window_height)


def init_spaceship():
    spaceship = Spaceship()
    spaceship.x = window_width/2
    spaceship.y = window_height/2
    spaceship.speed_x = 0
    spaceship.speed_y = 0
    spaceship.rotation = 0

    objects.append(spaceship)

def draw_all_objects():
    window.clear()

    for object in objects:
        object.draw()


init_spaceship()
window.push_handlers(on_draw=draw_all_objects)

pyglet.app.run()

