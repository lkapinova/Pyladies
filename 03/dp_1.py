from turtle import forward, left, right, exitonclick

for n in range (5,9):
    length = 200/n
    angle = 180-(180*(1-2/n))
    for i in range(n):
        forward(length)
        left(angle)
    forward(100)

exitonclick()
