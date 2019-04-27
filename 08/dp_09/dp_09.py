# Doplň funkci pohyb tak, aby zamezila:

# pohybu ven z mapy,
# pohybu na políčko, které už v seznamu je.
# Vhodná výjimka pro tyto situace je ValueError('Game over').

# Doplň i testy.

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
        if 0 > i > 9:
            raise ValueError('Game over')
    if nove_souradnice in seznam_souradnic:
        raise ValueError('Game over')

    del seznam_souradnic[0]
    seznam_souradnic.append(nove_souradnice)

souradnice = [(0, 0), (1, 0), (2, 0)]
pohyb(souradnice, 'j')      # [(1, 0), (2, 0), (2, 1)]
print(souradnice)        
pohyb(souradnice, 'z')      # [(2, 0), (2, 1), (1, 1)]
print(souradnice)         
pohyb(souradnice, 's')      # [(2, 1), (1, 1), (1, 0)]
print(souradnice)         
pohyb(souradnice, 'j')      #ValueError
print(souradnice)         
