from turtle import forward, left, right, exitonclick

n = 4
angle =  180-(180*(1-2/8))

for i in range(60):
    left(angle)
    forward(n)
    n = n+2

exitonclick()