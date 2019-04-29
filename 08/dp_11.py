# Hadí hřiště může mít libovolné rozměry větší než 4×1. Třeba 20×20 nebo 10×30.

import random


def nakresli_mapu(rozmer, souradnice_hada, souradnice_ovoce):
    """Funkce nakreslí čtvercovou mřížku zadaného rozměru.
    Na příslušná políčka uvedená v seznamu_souradnic doplní křížek."""

    x = rozmer[0]
    y = rozmer[1]

    mapa = []
    for _ in range(y):
        mapa.append(['.'] * x)

    for i in souradnice_hada:
        mapa[i[1]][i[0]] = 'x'

    for i in souradnice_ovoce:
        mapa[i[1]][i[0]] = '?'

    for i in mapa:
        for j in i:
            print(j, end=' ')
        print()
    print()


def pohyb(rozmer_mapy, souradnice_hada, svetova_strana, souradnice_ovoce, pocet_tahu):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""

    x = souradnice_hada[-1][0]
    y = souradnice_hada[-1][1]

    if svetova_strana == 's':
        y -= 1
    elif svetova_strana == 'j':
        y += 1
    elif svetova_strana == 'v':
        x += 1
    elif svetova_strana == 'z':
        x -= 1
    nove_souradnice = (x, y)

    for i in range(2):
        if nove_souradnice[i] < 0 or nove_souradnice[i] > (rozmer_mapy[i]-1):
            print('Hrál jsi ' + str(pocet_tahu) + ' tahů.')
            raise ValueError('Game over')

    if nove_souradnice in souradnice_hada:
        print('Hrál jsi ' + str(pocet_tahu) + ' tahů.')
        raise ValueError('Game over')

    if nove_souradnice in souradnice_ovoce:
        souradnice_ovoce.remove(nove_souradnice)
    else:
        del souradnice_hada[0]

    souradnice_hada.append(nove_souradnice)


def pridej_ovoce(rozmer_mapy, souradnice_hada, souradnice_ovoce):

    while True:
        x = random.randrange(rozmer_mapy[0])
        y = random.randrange(rozmer_mapy[1])
        nove_ovoce = (x, y)

        if nove_ovoce not in souradnice_hada and nove_ovoce not in souradnice_ovoce:
            souradnice_ovoce.append(nove_ovoce)
            break


rozmer_mapy = (3,4)
had = [(0, 0), (1, 0), (2, 0)]
svetove_strany = ['s', 'j', 'z', 'v']
ovoce = []
pocet_tahu = 0

pridej_ovoce(rozmer_mapy, had, ovoce)

while True:
    svetova_strana = input(
        "Zadej světovou stranu (s,j,v,z). Pokud už nechceš pokračovat, napiš exit.: ")

    if svetova_strana == 'exit':
        print('Hrál jsi ' + str(pocet_tahu) + ' tahů.')
        break

    if svetova_strana not in svetove_strany:
        print("Nezadal jsi svetovou stranu správně. Zkus to znovu.")
        continue

    pohyb(rozmer_mapy, had, svetova_strana, ovoce, pocet_tahu)

    if len(ovoce) == 0:
        pridej_ovoce(rozmer_mapy, had, ovoce)

    nakresli_mapu(rozmer_mapy, had, ovoce)

    pocet_tahu += 1
    if pocet_tahu % 30 == 0:
        pridej_ovoce(rozmer_mapy, had, ovoce)
