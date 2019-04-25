# Napiš funkci, která dostane seznam souřadnic (párů čísel menších než 10,
# která určují sloupec a řádek) a vypíše je jako mapu: mřížku 10×10,
# kde na políčka která jsou v seznamu napíše X, jinde tečku. Například:

# nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])
# X X . . . . . . . .
# . . . . . . . . . .
# . . X . . . . . . .
# . . . . X . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . . .
# . . . . . . . . X .
# Jak na to?

# Udělej tabulku (seznam seznamů) se samými tečkami, něco jako:
# [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']].
# Na příslušných místech nahraď tečky X-ky.
# Tabulku vypiš pomocí dvou cyklů for zanořených do sebe.


def nakresli_mapu(rozmer, seznam_souradnic):
    """Funkce nakreslí čtvercovou mřížku zadaného rozměru.
    Na příslušná políčka uvedená v seznamu_souradnic doplní křížek."""

    mapa = []
    for _ in range(rozmer):
        mapa.append(['.'] * rozmer)

    for i in seznam_souradnic:
        mapa[i[1]][i[0]] = 'x'

    for i in mapa:
        for j in i:
            print(j, end=' ')
        print()
    print()


nakresli_mapu(10, [(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (9, 8)])
nakresli_mapu(10, [(0, 1), (2, 3), (4, 8), (7, 2)])
nakresli_mapu(3, [(0,0), (1,1),(2,2)])
