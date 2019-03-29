import math
from turtle import forward, left, right, exitonclick, pencolor

def draw_house(sirka, vyska):
    pencolor("blue")
    uhlopricka = (sirka**2 + vyska**2)**(1/2)
    forward(sirka) #sirka
    left(90)
    forward(vyska) #vyska
    left(90)
    forward(sirka) #sirka
    right(180 - math.degrees(math.atan(vyska/sirka)))
    forward(1/2*uhlopricka) #1/2uhlopr
    right(2*math.degrees(math.atan(vyska/sirka)))
    forward(1/2*uhlopricka)  #1/2uhlopr
    right(180 - 2*math.degrees(math.atan(vyska/sirka)))
    forward(uhlopricka) #uhlopr
    right(90 + math.degrees(math.atan(vyska/sirka)))
    forward(vyska) #vyska
    right(90 + math.degrees(math.atan(vyska/sirka)))
    forward(uhlopricka) #uhlopr
    left(math.degrees(math.atan(vyska/sirka)))
    
draw_house(50, 70)
forward(20)
draw_house(30, 50)

exitonclick()