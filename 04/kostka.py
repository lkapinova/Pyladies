import random

# while True:
#     cislo = random.randint(1,6)
#     print(cislo)
#     if cislo == 6:
#         print("Konec hry!")
#         break

cislo = random.randint(1,6)
print(cislo)
while cislo != 6:
    cislo = random.randint(1,6)
    print(cislo)
print("Konec hry.")    

    