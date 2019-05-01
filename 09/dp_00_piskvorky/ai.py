import random
from util import tah

def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if "o-o" in herni_pole:
        policko = herni_pole.find("o-o")
        herni_pole = tah(herni_pole, (policko+1), 'o')
    elif "-oo" in herni_pole:
        policko = herni_pole.find("-oo")
        herni_pole = tah(herni_pole, policko, 'o')
    elif "oo-" in herni_pole:
        policko = herni_pole.find("oo-")
        herni_pole = tah(herni_pole, (policko+2), 'o')
    elif "x-x" in herni_pole:
        policko = herni_pole.find("x-x")
        herni_pole = tah(herni_pole, (policko+1), 'o')
    elif "-xx" in herni_pole:
        policko = herni_pole.find("-xx")
        herni_pole = tah(herni_pole, policko, 'o')
    elif "xx-" in herni_pole:
        policko = herni_pole.find("xx-")
        herni_pole = tah(herni_pole, (policko+2), 'o')
    elif "-x-" in herni_pole:
        policko = herni_pole.find("-x-")
        herni_pole = tah(herni_pole, (policko), 'o')
    else:
        delka_pole = len(herni_pole)
        while True:
            tah_pc = random.randrange(0, delka_pole)
            if herni_pole[tah_pc] == '-':
                herni_pole = tah(herni_pole, tah_pc, 'o')
                break

    return herni_pole



