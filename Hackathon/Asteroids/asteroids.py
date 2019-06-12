import pyglet
import images
from spaceship import Spaceship


window_width = 1000
window_height = 600


objects = []
keys_pressed = set()
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


def on_key_pressed(key, modifikatory):
    keys_pressed.add(key)
    print('Key pressed' + str(key))
    print('Keys currently presssed' + str(keys_pressed))


def on_key_released(key, modifikatory):
    keys_pressed.remove(key)
    print('Key release' + str(key))
    print('Keys currently presssed' + str(keys_pressed))


init_spaceship()
window.push_handlers(on_draw=draw_all_objects,
                     on_key_press=on_key_pressed, 
                     on_key_release=on_key_released)

pyglet.app.run()
