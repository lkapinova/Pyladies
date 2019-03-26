# komu padne dřív šestka
import random

print("Vítej ve hře s kostkou. Vítězí hráč, který bude potřebovat nejvíc hodů na to, aby mu padla šestka.")

def hod_kostkou_6 ():
    pocet_hodu = 1
    while True:
        hod = random.randint(1,6)
        print(hod)    
        if hod < 6:
            pocet_hodu += 1
        else:
            print("Hráč potřeboval", pocet_hodu, "hodů.")
            return (pocet_hodu)

pocet_hracu = 2
for i in range(pocet_hracu):
    pocet_hodu = hod_kostkou_6()

    
