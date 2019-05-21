import math
import pyglet

window = pyglet.window.Window(width=1000, height=700)


def tik(t):
    had.x += 1
    had.y += 2
    had.rotation = had.rotation + 10


pyglet.clock.schedule_interval(tik, 1/30)


def zpracuj_text(text):
    print(text)


obrazek = pyglet.image.load('had.png')
had = pyglet.sprite.Sprite(obrazek, y=5, x=5)


def vykresli():
    window.clear()
    had.draw()


window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
)


pyglet.app.run()
