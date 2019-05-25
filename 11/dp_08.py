import sys


class Vuz:
    def __init__(self, jmeno, kapacita, spz, spotreba):
        self.jmeno = jmeno
        self.kapacita = kapacita
        self.spz = spz
        self.spotreba = spotreba  # spotreba na 100 km, nafta l/100km; elektrina kWh/100km

    def __repr__(self):
        return f'Vuz: (\"{self.jmeno}\", kapacita {self.kapacita})'


class DieselVuz(Vuz):
    def je_dojezd_dostatecny(self, dojezd):
        return True

    def celkove_naklady(self, vzdalenost, cena_nafty, cena_elektriny):
        return vzdalenost * cena_nafty * self.spotreba/100


class ElektroVuz(Vuz):
    def __init__(self, jmeno, kapacita, spz, spotreba, dojezd):
        super().__init__(jmeno, kapacita, spz, spotreba)
        self.dojezd = dojezd    # dojezd na jendo nabiti

    def je_dojezd_dostatecny(self, dojezd):
        return self.dojezd >= dojezd

    def celkove_naklady(self, vzdalenost, cena_nafty, cena_elektriny):
        return vzdalenost * cena_elektriny * self.spotreba/100


class HybridVuz(Vuz):
    def __init__(self, jmeno, kapacita, spz, spotreba, dojezd):
        super().__init__(jmeno, kapacita, spz, spotreba)
        self.dojezd = dojezd    # dojezd na jendo nabiti

    def je_dojezd_dostatecny(self, dojezd):
        return True

    def celkove_naklady(self, vzdalenost, cena_nafty, cena_elektriny):
        if vzdalenost <= self.dojezd:
            return vzdalenost * cena_elektriny * self.spotreba/100
        else:
            return cena_elektriny * self.spotreba.spotreba_elektro/100 * self.dojezd + (vzdalenost - self.dojezd) * cena_nafty * self.spotreba.spotreba_diesel/100


class HybridVuzSpotreba():
    def __init__(self, spotreba_elektro, spotreba_diesel):
        self.spotreba_elektro = spotreba_elektro
        self.spotreba_diesel = spotreba_diesel


def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita


def najdi_vhodny_vuz(seznam_vozu, kapacita, delka_trasy, cena_nafty, cena_elektriny):
    vybrane_vozy = []
    for vuz in seznam_vozu:
        if vuz.kapacita >= kapacita and vuz.je_dojezd_dostatecny(delka_trasy):
            vybrane_vozy.append(vuz)
    if not vybrane_vozy:
        return None
    else:
        return min(vybrane_vozy, key=lambda vuz: vuz.celkove_naklady(delka_trasy, cena_nafty, cena_elektriny))


vozovy_park = [
    DieselVuz(jmeno='vuz1-D', kapacita=45, spz='1A1 1001', spotreba=30),
    ElektroVuz(jmeno='vuz2-E', kapacita=45,
               spz='1A1 1001', spotreba=45, dojezd=500),
    DieselVuz(jmeno='vuz3-D', kapacita=30, spz='1A2 1002', spotreba=25),
    ElektroVuz(jmeno='vuz4-E', kapacita=25,
               spz='1A3 1003', spotreba=35, dojezd=600),
    DieselVuz(jmeno='vuz5-D', kapacita=20, spz='1A4 1004', spotreba=20),
    ElektroVuz(jmeno='vuz6-E', kapacita=10,
               spz='1A5 1005', spotreba=25, dojezd=700),
    DieselVuz(jmeno='vuz7-D', kapacita=9, spz='1A6 1006', spotreba=10),
    ElektroVuz(jmeno='vuz8-E', kapacita=5,
               spz='1A7 1007', spotreba=15, dojezd=800),
    HybridVuz(jmeno='vuz9-H', kapacita=45, spz='1A8 1008',
              spotreba=HybridVuzSpotreba(30, 38), dojezd=400)
]

# print(vozovy_park)
print('Celkova kapacita vsech vozu je: ' +
      str(secti_celkovou_kapacitu(vozovy_park)))
print('Vhodny vuz: ' + str(najdi_vhodny_vuz(vozovy_park, 35, 600, 32.20, 4.9)))
