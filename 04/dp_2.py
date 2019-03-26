# komu padne dřív šestka
import random

print("Vítej ve hře s kostkou. Vítězí hráč, který bude potřebovat nejvíc hodů na to, aby mu padla šestka.")

def hod_kostkou_6 ():
    "Opakuje hod kostkou, dokud nepadne šestka. Sleduje počet hodů."
    pocet_hodu = 1
    while True:
        hod = random.randint(1,6)
        print(hod)    
        if hod < 6:
            pocet_hodu += 1
        else:
            print("Hráč potřeboval", pocet_hodu, "hodů.")
            return pocet_hodu

pocet_hracu = 4
max_pocet_hodu = 1
for i in range(pocet_hracu):
    pocet_hodu = hod_kostkou_6()
    if pocet_hodu > max_pocet_hodu:
        max_pocet_hodu = pocet_hodu
        hrac = i+1
print("Vyhrál hráč č.%d. Musel házet %dx." %(hrac, max_pocet_hodu))
    
    
