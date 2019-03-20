from turtle import forward, left, right, exitonclick

#květ
for i in range(18):
    for j in range(4):
        forward(50)
        left(90)
    left(20)

# stonek
right(90)
forward(100)

# větve vpravo
delka_vetvi = 10

for i in range (4):
    left(120)
    forward(2*delka_vetvi)

    for j in range (2):
        left(45)
        forward(delka_vetvi)
        left(180)
        forward(delka_vetvi)
        left(90)
        forward(delka_vetvi)
        left(180)
        forward(delka_vetvi)
        right(135)
        forward(2*delka_vetvi)

    left(180)
    forward(6*delka_vetvi)
    left(60)
    forward(50) 
    delka_vetvi += 5

# stonek
left(180)
forward(50)

# větve vlevo
delka_vetvi = 25

for i in range (4):
    left(60)
    forward(2*delka_vetvi)

    for j in range (2):
        left(45)
        forward(delka_vetvi)
        left(180)
        forward(delka_vetvi)
        left(90)
        forward(delka_vetvi)
        left(180)
        forward(delka_vetvi)
        right(135)
        forward(2*delka_vetvi)

    left(180)
    forward(6*delka_vetvi)
    left(120)
    forward(50) 
    delka_vetvi = delka_vetvi - 5

forward(50)

exitonclick()