from turtle import forward, left, right, exitonclick

length = 100
angle = 180 - (180/3)

for i in range(3):
    forward(length)
    left(angle)

exitonclick()
