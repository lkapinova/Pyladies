# napsal Tom, náhodný pohyb
import random
from turtle import forward, left, right, exitonclick, speed

n = 4
angle = 360 / n
length = 10
steps = 200

speed(1000)

random.seed()

for _ in range(steps):
    left(angle * random.randrange(n))
    forward(length)

exitonclick()