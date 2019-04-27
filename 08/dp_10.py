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


def pohyb(seznam_souradnic, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""

    x = seznam_souradnic[-1][0]
    y = seznam_souradnic[-1][1]

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
        if i < 0 or i > 9:
            raise ValueError('Game over')
    if nove_souradnice in seznam_souradnic:
        raise ValueError('Game over')

    del seznam_souradnic[0]
    seznam_souradnic.append(nove_souradnice)


def pohyb_po_ovoci(seznam_souradnic, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""

    x = seznam_souradnic[-1][0]
    y = seznam_souradnic[-1][1]

    if svetova_strana == 's':
        y -= 1
    elif svetova_strana == 'j':
        y += 1
    elif svetova_strana == 'v':
        x += 1
    elif svetova_strana == 'z':
        x -= 1
    nove_souradnice = (x, y)
    seznam_souradnic.append(nove_souradnice)


def pridej_ovoce(rozmer_mapy, souradnice_hada, souradnice_ovoce):

    while True:
        x = random.randrange(rozmer_mapy)
        y = random.randrange(rozmer_mapy)
        nove_ovoce = (x, y)

        if nove_ovoce not in souradnice_hada:
            souradnice_ovoce.append(nove_ovoce)
            break


rozmer_mapy = 10
had = [(0, 0), (1, 0), (2, 0)]
svetove_strany = ['s', 'j', 'z', 'v']
ovoce = []


while True:
    svetova_strana = input(
        "Zadej světovou stranu (s,j,v,z). Pokud už nechceš pokračovat, napiš exit.: ")
    if svetova_strana == 'exit':
        break
    elif svetova_strana not in svetove_strany:
        print("Nezadal jsi svetovou stranu správně. Zkus to znovu.")
        continue
    else:
        pridej_ovoce(rozmer_mapy, had, ovoce)
        pohyb(had, svetova_strana)
        nakresli_mapu(rozmer_mapy, had, ovoce)
