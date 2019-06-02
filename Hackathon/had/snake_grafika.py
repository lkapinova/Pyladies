import pyglet
import random
import snake_tiles
from pyglet.window import key
from pathlib import Path


square_side = 64
width = 15
height = 10
picture = snake_tiles.snake_tiles['tail-head']
picture_apple = pyglet.image.load('red.png')
svetova_strana = 'v'
game_is_running = True


class Pixel():

    def __init__(self, picture, x, y):
        self.picture = picture
        self.coord_x = x
        self.coord_y = y

    def __repr__(self):
        return f"({self.coord_x},{self.coord_y})"

    def __eq__(self, other):
        return self.coord_x == other.coord_x and self.coord_y == other.coord_y

    def set_picture(self, picture):
        self.picture = picture


class Apple(Pixel):

    def __init__(self, picture, x, y):
        self.picture = picture_apple
        self.coord_x = x
        self.coord_y = y


def place_pixels():
    """Funkce vykresluje po pixelech hada i ovoce""" 

    window.clear()
    vector2name = {(-1, 0): 'left', (1, 0): 'right',
                   (0, 1): 'top', (0, -1): 'bottom'}

    # hlava
    delta_x = snake_coords[-2].coord_x - snake_coords[-1].coord_x
    delta_y = snake_coords[-2].coord_y - snake_coords[-1].coord_y
    delta = (delta_x, delta_y)
    direction = vector2name[delta]
    piece = pyglet.sprite.Sprite(
        snake_tiles.snake_tiles[direction+'-tongue'], snake_coords[-1].coord_x*square_side, snake_coords[-1].coord_y*square_side)
    piece.draw()

    # ocas
    delta_x = snake_coords[1].coord_x - snake_coords[0].coord_x
    delta_y = snake_coords[1].coord_y - snake_coords[0].coord_y
    delta = (delta_x, delta_y)
    direction = vector2name[delta]
    piece = pyglet.sprite.Sprite(
        snake_tiles.snake_tiles['tail-'+direction], snake_coords[0].coord_x*square_side, snake_coords[0].coord_y*square_side)
    piece.draw()

    # tělo
    for i in range(1, len(snake_coords)-1):
        r_delta_x = snake_coords[i+1].coord_x - snake_coords[i].coord_x
        r_delta_y = snake_coords[i+1].coord_y - snake_coords[i].coord_y
        l_delta_x = snake_coords[i-1].coord_x - snake_coords[i].coord_x
        l_delta_y = snake_coords[i-1].coord_y - snake_coords[i].coord_y
        r_delta = (r_delta_x, r_delta_y)
        l_delta = (l_delta_x, l_delta_y)
        r_direction = vector2name[r_delta]
        l_direction = vector2name[l_delta]
        piece = pyglet.sprite.Sprite(
            snake_tiles.snake_tiles[l_direction + '-' + r_direction], snake_coords[i].coord_x*square_side, snake_coords[i].coord_y*square_side)
        piece.draw()


    # jablka
    for item in apples_coords:
        piece = pyglet.sprite.Sprite(
            item.picture, item.coord_x*square_side, item.coord_y*square_side)
        piece.draw()


def pohyb(seznam_poli, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru.
     Prodlužuje hada, pokud sní ovoce, a ukončuje hru, pokud had vyleze z herního plánu."""

    global game_is_running

    x = seznam_poli[-1].coord_x
    y = seznam_poli[-1].coord_y
    # print(x,y)

    if svetova_strana == 's':
        y += 1
    elif svetova_strana == 'j':
        y -= 1
    elif svetova_strana == 'v':
        x += 1
    elif svetova_strana == 'z':
        x -= 1

    new_snake_pixel = Pixel(picture, x, y)

    if x <= -1 or x > width-1 or y <= -1 or y > height-1:
        game_is_running = False
        return

    # pro porovnani se seznamem ovoce
    new_pixel = Apple(picture, x, y)
    if new_pixel in apples_coords:
        apples_coords.remove(new_pixel)
    else:
        del seznam_poli[0]

    if new_snake_pixel in seznam_poli:
        game_is_running = False

    seznam_poli.append(new_snake_pixel)


def stisk_klavesy(symbol, modifikatory):
    """Převod stisku kláves na světové strany"""
    global svetova_strana
    if symbol == key.UP:
        svetova_strana = 's'
    if symbol == key.DOWN:
        svetova_strana = 'j'
    if symbol == key.LEFT:
        svetova_strana = 'z'
    if symbol == key.RIGHT:
        svetova_strana = 'v'


def add_apple(snake_coords, apples_coords):
    """Funkce přidává ovoce tak, aby v herním plánu byly vždy tři kusy ovoce."""
    while len(apples_coords) < 3:
        x = random.randrange(width-1)
        y = random.randrange(height-1)
        new_apple = Apple(picture_apple, x, y)
        if new_apple not in snake_coords and new_apple not in apples_coords:
            apples_coords.append(new_apple)


def tik(time):
    """Volání fukncí v jednom tiku"""
    if game_is_running:
        add_apple(snake_coords, apples_coords)
        pohyb(snake_coords, svetova_strana)
        # print(snake_coords)


# vstupn9 data
snake_coords = [Pixel(picture, 3, 5), Pixel(
    picture, 4, 5), Pixel(picture, 5, 5)]
apples_coords = []

# hra, pyglet
add_apple(snake_coords, apples_coords)
pyglet.clock.schedule_interval(tik, 1/2)
window = pyglet.window.Window(
    width=width*square_side, height=height*square_side)
window.push_handlers(on_draw=place_pixels,
                     on_key_press=stisk_klavesy)

pyglet.app.run()
