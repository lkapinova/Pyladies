# Přidej do hry hadí potravu. Tady jsou pravidla pro vegetariánského hada, ale můžeš si je změnit podle chuti:

# Seznam ovoce obsahuje na začátku jedno ovoce na políčku,
# na kterém není had (například: [(2, 3)] znamená jedno ovoce na pozici (2, 3)).
# Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to, cos přidala v projektu 13),
# a pokud na mapě zrovna není další ovoce, na náhodném místě (kde není had) vyroste ovoce nové.

# Každých 30 tahů vyroste nové ovoce samo od sebe.
# Na mapě se toto tajemné ovoce zobrazuje jako otazník (?).

import random


def nakresli_mapu(rozmer, souradnice_hada, souradnice_ovoce):
    """Funkce nakreslí čtvercovou mřížku zadaného rozměru.
    Na příslušná políčka uvedená v seznamu_souradnic doplní křížek."""

    mapa = []
    for _ in range(rozmer):
        mapa.append(['.'] * rozmer)

    for i in souradnice_hada:
        mapa[i[1]][i[0]] = 'x'

    for i in souradnice_ovoce:
        mapa[i[1]][i[0]] = '?'

    for i in mapa:
        for j in i:
            print(j, end=' ')
        print()
    print()


def pohyb(souradnice_hada, svetova_strana, souradnice_ovoce, pocet_tahu):
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

    for i in nove_souradnice:
        if i < 0 or i > (rozmer_mapy - 1):
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
        x = random.randrange(rozmer_mapy)
        y = random.randrange(rozmer_mapy)
        nove_ovoce = (x, y)

        if nove_ovoce not in souradnice_hada and nove_ovoce not in souradnice_ovoce:
            souradnice_ovoce.append(nove_ovoce)
            break


rozmer_mapy = 4
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

    pohyb(had, svetova_strana, ovoce, pocet_tahu)

    if len(ovoce) == 0:
        pridej_ovoce(rozmer_mapy, had, ovoce)

    nakresli_mapu(rozmer_mapy, had, ovoce)

    pocet_tahu += 1
    if pocet_tahu % 30 == 0:
        pridej_ovoce(rozmer_mapy, had, ovoce)
