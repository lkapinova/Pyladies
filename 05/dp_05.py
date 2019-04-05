# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným tahem počítače.

# Použij jednoduchou náhodnou „strategii”:

# Vyber číslo od 0 do 19.
# Pokud je dané políčko volné, hrej na něj.
# Pokud ne, opakuj od bodu 1.

import random

def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    while True:
        tah_pc = random.randint(0,19)
        if herni_pole[tah_pc] == '-':
            herni_pole = herni_pole[:tah_pc] + 'o' + herni_pole[(tah_pc+1):]
            break
        else:
            continue
    return herni_pole

print(tah_pocitace('-'*20))
print(tah_pocitace('x---xx---xx---xx---x'))