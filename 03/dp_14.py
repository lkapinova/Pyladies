import math
from math import pi, sin
from turtle import forward, left, right, exitonclick, penup, pendown
from random import randrange

# výpočet délky strany pěticípé hvězdy
length = 20*sin(pi/2)/sin(pi-3*pi/(2*5))

# výpočet úhlů
alfa = (2*pi/5)*180/pi
beta = 180 - (pi/5)*180/pi

for i in range(10):

    # hvězda
    forward(length)
    left(beta)
    forward(length)
    right(alfa)
    forward(length)
    left(beta)
    forward(length)
    right(alfa)
    forward(length)
    left(beta)
    forward(length)
    right(alfa)
    forward(length)
    left(beta)
    forward(length)
    right(alfa)
    forward(length)
    left(beta)
    forward(length)

    # otočení kurzoru a cesta zpět do cípu hvězdy
    right(180)
    forward(length)

    # náhodný výběr vzdálenosti a úhlu
    length_for_move = randrange(100, 200)
    angle_for_move = randrange(0, 360)


    # přesun kurzoru na jiné místo
    penup()
    forward(length_for_move)
    right(angle_for_move)
    pendown()


exitonclick()
