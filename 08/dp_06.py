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

def pohyb(souradnice, svetova_strana):

    