# Napiš cyklus, který se bude ptát uživatele na světovou stranu, podle ní zavolá pohyb,
# a následně vykreslí seznam jako mapu. Pak se opět se zeptá na stranu atd.

# Začínej se seznamem [(0, 0), (1, 0), (2, 0)].


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


def pohyb(seznam_souradnic, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""

    for i in seznam_souradnic:
        x = i[0]
        y = i[1]

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


seznam = [(0, 0), (1, 0), (2, 0)]
rozmer_mapy = 10

while True:
    svetova_strana = input(
        "Zadej světovou stranu (s,j,v,z). Pokud už nechceš pokračévat, napiš exit.: ")
    if svetova_strana == 'exit':
        break
    else:
        pohyb(seznam, svetova_strana)
        nakresli_mapu(rozmer_mapy, seznam)
