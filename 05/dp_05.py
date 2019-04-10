# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

# Použij jednoduchou náhodnou „strategii”:

# Vyber číslo od 0 do 19.
# Pokud je dané políčko volné, hrej na něj.
# Pokud ne, opakuj od bodu 1.

import random

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    
    herni_pole = pole[:cislo_policka] + symbol + pole[(cislo_policka+1):]
    return herni_pole

def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    delka_pole = len(herni_pole)
    while True:
        tah_pc = random.randrange(0,delka_pole)
        if herni_pole[tah_pc] == '-':
            herni_pole = tah(herni_pole, tah_pc, 'o')
            break
    return herni_pole

print(tah_pocitace('-'*20))
print(tah_pocitace('x---xx---xx---xx---x'))
