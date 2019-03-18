from turtle import forward, left, right, exitonclick

# pravidelny n-uhelnik

n = int(input("Budeme kreslit n-uhelniky. Zadej pocet vrcholu, ktery bude mit tvuj n-uhelnik: "))

length = 200/n
angle = 180-(180*(1-2/n))
for i in range(n):
    forward(length)
    left(angle)

exitonclick()
