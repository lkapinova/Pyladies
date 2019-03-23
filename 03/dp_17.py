print("Tento program vybere z pěti, tebou zadaných čísel nejmenší.")

a = input("Zadej první číslo: ")
b = input("Zadej druhé číslo: ")
c = input("Zadej třetí číslo: ")
d = input("Zadej čtvrté číslo: ")
e = input("Zadej páté číslo: ")

if a <= b:
    if a <= c:
        if a <= d:
            if a <= e:
                print("Nejmenší číslo je ", a)

if b <= a:
    if b <= c:
        if b <= d:
            if b <= e:
                print("Nejmenší číslo je ", b)

if c <= a:
    if c <= b:
        if c <= d:
            if c <= e:
                print("Nejmenší číslo je ", c)

if d <= a:
    if d <= b:
        if d <= c:
            if d <= e:
                print("Nejmenší číslo je ", d)

if e <= a:
    if e <= b:
        if e <= c:
            if e <= d:
                print("Nejmenší číslo je ", e)
