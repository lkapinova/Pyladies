import random

pocet_bodu = 0

# prvni kolo
karta = random.randint(2,10)
pocet_bodu = pocet_bodu + karta
print(pocet_bodu)

# bude se pokracovat?
while pocet_bodu < 21:
    dalsi_kolo = input("Chces pokracovat (ano/ne): ")
    if dalsi_kolo == "ano":
        karta = random.randint(2,10)
        print("karta: " + str(karta))
        pocet_bodu = pocet_bodu + karta
        print("pocet bodu: " + str(pocet_bodu))
    elif dalsi_kolo == "ne":
        print("pocet bodu" + str(pocet_bodu))
        break
    else:
        print("Nerozumim. Odpovidej ano nebo ne.")
    
# vyhodnoceni
if pocet_bodu < 21:
    print("Už jen kousek.")
elif pocet_bodu == 21:
    print("Parada, mas to presne.")
else:
    print("Treba priste.")
