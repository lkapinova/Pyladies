import pyglet


square_side = 64
picture = pyglet.image.load('green.png')


class Snake():

    def __init__(self, picture, x, y):
        self.picture = picture
        self.coord_x = x*square_side
        self.coord_y = y*square_side


def place_snake():
    window.clear()

    for item in snake_coords:
        piece = pyglet.sprite.Sprite(item.picture, item.coord_x, item.coord_y)
        piece.draw()


snake_coords = [Snake(picture, 4, 5), Snake(picture, 5, 5)]

window = pyglet.window.Window(width=15*square_side, height=10*square_side)
window.push_handlers(on_draw=place_snake)

pyglet.app.run()
