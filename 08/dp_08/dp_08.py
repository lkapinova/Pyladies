# Doplň funkci pohyb tak, aby při pohybu umazala první bod ze seznamu souřadnic.
# Výsledný seznam tak bude mít stejnou délku, jako před voláním.

# Uprav testy.


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

    del seznam_souradnic[0]
    seznam_souradnic.append(nove_souradnice)


souradnice = [(0, 0), (1, 0), (2, 0)]
pohyb(souradnice, 'j')
print(souradnice)         # → [(1, 0), (2, 0), (2, 1)]
pohyb(souradnice, 's')
print(souradnice)         # → [(2, 0), (2, 1), (2, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(2, 1), (2, 0), (3, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(2, 0), (3, 0), (4, 0)]
