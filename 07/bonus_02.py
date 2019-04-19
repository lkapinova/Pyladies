# Napis funkci, ktera dostane seznam a vrati z neho 
# seznam o dvou nahodnych prvcich z puvodniho seznamu

import random

seznam = []
for i in range(25):
    seznam.append(random.randint(0,1000))
print(seznam)

def vyber_dva(seznam):
    "Funkce vybere dva prvky ze seznamu a vlozi je do noveho."

    novy_seznam = random.choices(seznam,k=2)
    return novy_seznam

print(vyber_dva(seznam))