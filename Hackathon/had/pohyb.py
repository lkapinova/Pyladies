def pohyb(seznam_poli, svetova_strana):
    """Funkce ze seznamu souřadnic a světové strany (zadané jako: "s", "j", "v" nebo "z")
     a přidá k seznamu souřadnice bodu posunutý v zadaném směru."""

    x = seznam_poli[-1].coord_x
    y = seznam_poli[-1].coord_y

    if svetova_strana == 's':
        y -= 1
    elif svetova_strana == 'j':
        y += 1
    elif svetova_strana == 'v':
        x += 1
    elif svetova_strana == 'z':
        x -= 1

    nove_pole = Snake(picture, x, y)

    del seznam_poli[0]
    seznam_poli.append(nove_pole)


