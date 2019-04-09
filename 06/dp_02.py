# Napiš program, který načte číslo a zjistí, jestli je sudé.

# Sudá čísla jsou beze zbytku dělitelná dvěma.

import random

def sude_liche_cislo(cislo):
    "Tato funkce zjisti, zda je cislo sude nebo liche."

    if cislo % 2 == 0:
        print('{} je sude cislo.'.format(cislo))
    else:
        print('{} je liche cislo.'.format(cislo))

sude_liche_cislo(1212)
sude_liche_cislo(121)
sude_liche_cislo(random.randint(0,10000))
