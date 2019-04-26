# Napiš funkci pohyb, která dostane seznam souřadnic a světovou stranu ("s", "j", "v" nebo "z")
# a přidá k seznamu poslední bod „posunutý“ v daném směru.
# Např.:

# souradnice = [(0, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0)]
# pohyb(souradnice, 'v')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
# pohyb(souradnice, 'j')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
# pohyb(souradnice, 's')
# print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
# Funkce by neměla nic vracet. Jen mění už existující seznam.

# Nezapomeň na testy.


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


souradnice = [(0, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0)]
pohyb(souradnice, 'v')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0)]
pohyb(souradnice, 'j')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1)]
pohyb(souradnice, 's')
print(souradnice)         # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
