import pyglet
from pyglet.window import key


square_side = 64
width = 15
height = 10
picture = pyglet.image.load('green.png')
svetova_strana = 'v'
game_is_running = True


class Snake():

    def __init__(self, picture, x, y):
        self.picture = picture
        self.coord_x = x
        self.coord_y = y

    def __repr__(self):
        return f"({self.coord_x},{self.coord_y})"

    def __eq__(self, other):
        return self.coord_x == other.coord_x and self.coord_y == other.coord_y


def place_snake():
    window.clear()

    for item in snake_coords:
        piece = pyglet.sprite.Sprite(
            item.picture, item.coord_x*square_side, item.coord_y*square_side)
        piece.draw()


def pohyb(seznam_poli, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""
    
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

    nove_pole = Snake(picture, x, y)

    if x <= -1 or x > width-1 or y <= -1 or y > height-1:  
        game_is_running = False
        return

    del seznam_poli[0]

    if nove_pole in seznam_poli:
        game_is_running = False
        

    seznam_poli.append(nove_pole)


def stisk_klavesy(symbol, modifikatory):
    global svetova_strana
    if symbol == key.UP:
        svetova_strana = 's'
    if symbol == key.DOWN:
        svetova_strana = 'j'
    if symbol == key.LEFT:
        svetova_strana = 'z'
    if symbol == key.RIGHT:
        svetova_strana = 'v'


def tik(time):
    if game_is_running:
        pohyb(snake_coords, svetova_strana)


snake_coords = [Snake(picture, 0, 5), Snake(picture, 1, 5), Snake(
    picture, 2, 5), Snake(picture, 3, 5), Snake(picture, 4, 5), Snake(picture, 5, 5)]


pyglet.clock.schedule_interval(tik, 1)
window = pyglet.window.Window(
    width=width*square_side, height=height*square_side)
window.push_handlers(on_draw=place_snake,
                     on_key_press=stisk_klavesy)

pyglet.app.run()
