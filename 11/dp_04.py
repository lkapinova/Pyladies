class Vuz:
    def __init__(self, jmeno, kapacita, spz, naklady):
        self.jmeno = jmeno
        self.kapacita = kapacita
        self.spz = spz

    def __repr__(self):
        return f'Vuz(\"{self.jmeno}\", {self.kapacita})'


vozovy_park = [
    Vuz(jmeno='vuz1', kapacita=45, spz='1A1 1001', naklady=30),
    Vuz(jmeno='vuz2', kapacita=30, spz='1A2 1002', naklady=25),
    Vuz(jmeno='vuz3', kapacita=25, spz='1A3 1003', naklady=20),
    Vuz(jmeno='vuz4', kapacita=20, spz='1A4 1004', naklady=15),
    Vuz(jmeno='vuz5', kapacita=10, spz='1A5 1005', naklady=11),
    Vuz(jmeno='vuz6', kapacita=9, spz='1A6 1006', naklady=10),
    Vuz(jmeno='vuz7', kapacita=5, spz='1A7 1007', naklady=8)
]


def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita


def najdi_podle_kapacity(seznam_vozu, kapacita):
    vybrane_vozy = []
    for vuz in seznam_vozu:
        if vuz.kapacita >= kapacita:
            vybrane_vozy.append(vuz)
    return vybrane_vozy


def vypis_SPZ(seznam_vozu):
    for vuz in seznam_vozu:
        print(vuz.spz)


def all_SPZ(seznam_vozu):
    spz_list = []
    for vuz in seznam_vozu:
        spz_list.append(vuz.spz)
    return spz_list


# print('Celkova kapacita vsech vozu je: '+ str(secti_celkovou_kapacitu(vozovy_park)))
# print(najdi_podle_kapacity(vozovy_park, 25))
vypis_SPZ(vozovy_park)
print()
print('\n'.join(all_SPZ(vozovy_park)))
