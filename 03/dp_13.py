from turtle import forward, left, right, exitonclick

n = 0.1
angle = 180-(180*(1-2/100))

for i in range(1000):
    left(angle)
    forward(n)
    n = n + 0.01   

exitonclick()