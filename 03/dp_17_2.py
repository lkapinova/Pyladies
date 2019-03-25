print("Tento program vybere z pěti, tebou zadaných čísel nejmenší.")

a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))
c = int(input("Zadej třetí číslo: "))
d = int(input("Zadej čtvrté číslo: "))
e = int(input("Zadej páté číslo: "))


min = a
if b < min:
    min = b
if c < min:
    min = c
if d < min:
    min = d
if e < min:
    min = e

print("Nejmenší číslo je ", min)




