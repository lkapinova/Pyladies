# Zvládneš pro počítač naprogramovat lepší strategii? 
# Třeba aby se snažil hrát vedle svých existujících symbolů nebo aby bránil protihráčovi?


import random

def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    
    herni_pole = pole[:cislo_policka] + symbol + pole[(cislo_policka+1):]
    return herni_pole

def tah_hrace(herni_pole):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    while True:
        tvuj_tah = input("Kam chces umistit svuj symbol? ")

        if not tvuj_tah.isdigit():
            print("Nezadal jsi cislo.")
            continue
        
        tvuj_tah = int(tvuj_tah)

        if tvuj_tah not in range(len(herni_pole)):
            print("Bohuzel, netrefil ses do herniho pole.")
            continue

        elif herni_pole[tvuj_tah] != '-':
            print("Smula, policko uz je zabrane.")
            continue

        else:
            return tah(herni_pole, tvuj_tah, 'x')


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
            tah_pc = random.randint(0,delka_pole)
            if herni_pole[tah_pc] == '-':
                herni_pole = tah(herni_pole, tah_pc, 'o')
                break
   
    return herni_pole

def vyhodnot(piskvorky):
    "Funkce vyhodnotí 1D piškvorky. Pro vítězství jsou nutné tři znaky v řadě."

    if "xxx" in piskvorky:
        vysledek = 'x'
    elif "ooo" in piskvorky:
        vysledek = 'o'
    elif "-" not in piskvorky:
        vysledek = "!"
    else:
        vysledek = '-'
    return vysledek

def piskvorky1d(herni_pole):
    "Funkce vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze."

    while True:
        herni_pole = tah_hrace(herni_pole)
        print(herni_pole)
        if vyhodnot(herni_pole) == 'x':
            print('Gratuji, vyhral si!')
            break
        elif vyhodnot(herni_pole) == '!':
            print('Je to remiza.')
            break
        
        herni_pole = tah_pocitace(herni_pole)
        print(herni_pole)
        if vyhodnot(herni_pole) == 'o':
            print('Smula,  vyhrava pocitac.')
            break
        elif vyhodnot(herni_pole) == '!':
            print('Je to remiza.')
            break
       

piskvorky1d(20*'-')
        

