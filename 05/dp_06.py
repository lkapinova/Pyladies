# Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a 
# střídavě volá funkce tah_hrace a tah_pocitace, 
# dokud někdo nevyhraje nebo nedojde k remíze.

# Nezapomeň kontrolovat stav hry po každém tahu.

import random

def tah_hrace(herni_pole):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    while True:
        tvuj_tah = input("Kam chces umistit svuj symbol? ")
        if tvuj_tah.isdigit():
            tvuj_tah = int(tvuj_tah)
            if tvuj_tah >= 0 and tvuj_tah <= 19:
                if herni_pole[tvuj_tah] == '-':
                    herni_pole = herni_pole[:tvuj_tah] + 'x' + herni_pole[(tvuj_tah+1):]
                elif herni_pole[tvuj_tah] != '-':
                    print("Smula, policko uz je zabrane.")
                    continue
            else:
                print("Bohuzel, netrefil ses do herniho pole.")
                continue
        else:
            print("Co delas?! Hrajeme piskovorky! Zkus to znovu.")
            continue
        return herni_pole


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

def vyhodnot(piskvorky):
    "Funkce vyhodnotí 1D piškvorky. Pro vítězství jsou nutné tři znaky v řadě."

    if "xxx" in piskvorky:
        vysledek = 'x'
    elif "ooo" in piskvorky:
        vysledek = 'o'
    elif "-" not in piskvorky and "xxx" not in piskvorky and "ooo" not in piskvorky:
        vysledek = "!"
    else:
        vysledek = '-'
    return vysledek

def piskvorky1d():
    herni_pole = 20*'-'
    
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
       

piskvorky1d()
        

