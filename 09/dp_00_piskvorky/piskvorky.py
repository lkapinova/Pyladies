from ai import tah_pocitace
from util import tah


def tah_hrace(herni_pole):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    while True:
        tvuj_tah = input("Kam chces umistit svuj symbol? ")

        if not tvuj_tah.isdigit():
            print("Nezadal jsi cislo.")
            continue

        tvuj_tah = int(tvuj_tah)

        if not (0 <= tvuj_tah < len(herni_pole)):
            print("Bohuzel, netrefil ses do herniho pole.")

        elif herni_pole[tvuj_tah] != '-':
            print("Smula, policko uz je zabrane.")

        else:
            herni_pole = tah(herni_pole, tvuj_tah, 'x')
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
