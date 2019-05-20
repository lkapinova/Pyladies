class Vuz:
    def __init__(self, jmeno, kapacita, spz, naklady):
        self.jmeno = jmeno
        self.kapacita = kapacita
        self.spz = spz
        self.naklady = naklady  # naklady vozu na 1 km

    def __repr__(self):
        return f'Vuz: (\"{self.jmeno}\", kapacita {self.kapacita})'


class DieselVuz(Vuz):

    def je_dojezd_dostatecny(self, dojezd):
        return True


class ElektroVuz(Vuz):
    def __init__(self, jmeno, kapacita, spz, naklady, dojezd):
        self.jmeno = jmeno
        self.kapacita = kapacita
        self.spz = spz
        self.naklady = naklady  # naklady vozu na 1 km
        self.dojezd = dojezd    # dojezd na jendo nabiti

    def je_dojezd_dostatecny(self, dojezd):
        return self.dojezd >= dojezd


class HybridVuz(Vuz):

    def je_dojezd_dostatecny(self, dojezd):
        return True

    # def vypocti_naklady(self, delka_trasy):


def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita


def najdi_vhodny_vuz(seznam_vozu, kapacita, delka_trasy):
    nejlevnejsi_naklady = 10000
    for vuz in seznam_vozu:
        if vuz.kapacita >= kapacita and vuz.je_dojezd_dostatecny(delka_trasy):
            if vuz.naklady < nejlevnejsi_naklady:
                vybrany_vuz = vuz
                nejlevnejsi_naklady = vuz.naklady

    return vybrany_vuz


vozovy_park = [
    DieselVuz(jmeno='vuz1-D', kapacita=45, spz='1A1 1001', naklady=30),
    ElektroVuz(jmeno='vuz2-E', kapacita=45,
               spz='1A1 1001', naklady=20, dojezd=500),
    DieselVuz(jmeno='vuz3-D', kapacita=30, spz='1A2 1002', naklady=25),
    ElektroVuz(jmeno='vuz4-E', kapacita=25,
               spz='1A3 1003', naklady=15, dojezd=600),
    DieselVuz(jmeno='vuz5-D', kapacita=20, spz='1A4 1004', naklady=15),
    ElektroVuz(jmeno='vuz6-E', kapacita=10,
               spz='1A5 1005', naklady=8, dojezd=700),
    DieselVuz(jmeno='vuz7-D', kapacita=9, spz='1A6 1006', naklady=10),
    ElektroVuz(jmeno='vuz8-E', kapacita=5,
               spz='1A7 1007', naklady=6, dojezd=800)
]

# print(vozovy_park)
print('Celkova kapacita vsech vozu je: ' +
      str(secti_celkovou_kapacitu(vozovy_park)))
print('Vhodny vuz: ' + str(najdi_vhodny_vuz(vozovy_park, 25, 350)))
