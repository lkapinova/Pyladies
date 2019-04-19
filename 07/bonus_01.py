# Napis funkci, ktera dostane seznam, odstrani posledni dva prvky 
# a zbytek vrati jako setrideny seznam

import random

seznam = []
for i in range(25):
    seznam.append(random.randint(0,1000))
print(seznam)

# seznam = [13, 668, 48, 754, 376, 808, 982, 762, 945, 771, 904, 140, 413, 488, 298, 961, 730, 124, 584, 564, 535, 944, 628, 27, 106]

def uprava_listu(list):
    "Tato funkce vymaze ze seznamu prvni dva prvky a zbyle prvky seradi."
    list = list[2:]
    list.sort()
    return list

print(uprava_listu(seznam))
