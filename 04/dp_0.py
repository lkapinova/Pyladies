from turtle import forward, left, right, exitonclick, pencolor

def draw_house(size):
    pencolor("blue")
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    right(120)
    forward(size)
    right(120)
    forward(size)
    right(75)
    forward(2**(1/2)*size)
    right(135)
    forward(size)
    right(135)
    forward(2**(1/2)*size)
    left(45)
    # forward(size)
   
draw_house(125)
forward(20)
draw_house(25)

exitonclick()