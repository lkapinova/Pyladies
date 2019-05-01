# Rozděl 1D Piškvorky na čtyři moduly:

# ai.py, kde bude funkce tah_pocitace,
# piskvorky.py, kde budou ostatní funkce,
# hra.py, kde bude import a volání hlavní funkce z piskvorky.py (a nic jiného),
# test_piskvorky.py, kde budou testy.
# Jak se do importů nezamotat? Podívej se do materiálů na sekci cyklické importy.

# Pokud jsi byla na workshopu Gitu, dej to do Gitu! A kdybys něco nedopatřením rozbila, 
# git diff HEAD ukáže změny od poslední revize.



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
        
        tvuj_tah = int(tvuj_tah)

        if not (0 <= tvuj_tah < len(herni_pole)):
            print("Bohuzel, netrefil ses do herniho pole.")

        elif herni_pole[tvuj_tah] != '-':
            print("Smula, policko uz je zabrane.")

        else:
            return tah(herni_pole, tvuj_tah, 'x')

def tah_pocitace(herni_pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    delka_pole = len(herni_pole)
    while True:
        tah_pc = random.randrange(0,delka_pole)
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
            print('Smula, vyhrava pocitac.')
            break
        elif vyhodnot(herni_pole) == '!':
            print('Je to remiza.')
            break
       

piskvorky1d(20*'-')
        
