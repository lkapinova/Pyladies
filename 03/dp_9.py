from turtle import forward, left, right, exitonclick

n = 95

length = 200/n
angle = 180-(180*(1-2/n))
for i in range(n):
    forward(length)
    left(angle)

exitonclick()