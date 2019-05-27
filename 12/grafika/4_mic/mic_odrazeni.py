import pyglet

window = pyglet.window.Window(width=1000, height=700)
micek = pyglet.image.load("C:\\Users\\lenka\\main\\git\\Pyladies\\12\\grafika\\obrazky\\micek.png")

# (1) TODO: Vytvorit tridu Micek. Obsahovat bude odkaz na objekt na platne a rychlost tohoto objektu na obou osach rychlost_x a rychlost_y
# (2) TODO: Rychlost na obou osach prijimat jako parametr


class Micek():
    
    def __init__(self, rychlost_x, rychlost_y):
        self.objekt = pyglet.sprite.Sprite(micek)
        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y


objekty = []
# (3) TODO: Do seznamu objektu vlozit instanci objektu Micek
m1 = Micek(3, 3)
m2 = Micek(1, 2)
objekty.append(m1)
objekty.append(m2)

def vykresli():
    window.clear()

    # (4) TODO: Vykresli vsechny elementy ze seznamu objektu. (Teckovou notaci se dostaneme k jakekoliv vlastnosti objektu)
    for element in objekty:
        element.objekt.draw()


def pohyb(dt):
    # (5) TODO: Pri kazdem tiku posunu kazdy z elementu na ose X i Y
    for element in objekty:
        element.objekt.x += element.rychlost_x
        element.objekt.y += element.rychlost_y
        
       # element.rychlost_y -= 1


    # (6) TODO: Pokud se element dostane na okraj okna, odrazi se (take na obou osach)
        if element.objekt.x < 0 or element.objekt.x > window.width - element.objekt.width:
            element.rychlost_x = - element.rychlost_x    
        if element.objekt.y < 0 or element.objekt.y > window.height - element.objekt.height:
            element.rychlost_y = - element.rychlost_y
              

pyglet.clock.schedule_interval(pohyb, 1/60)
window.push_handlers(on_draw=vykresli)
pyglet.app.run()

# (BONUS) TODO: Do pohybu zakomponujte i gravitaci (micky budou stale vice pritahovany k zemi)
# (BONUS) TODO: Pro velmi sikovne jedince: muzete doprogramovat kontrolu, ktera vyresi srazku dvou micku
