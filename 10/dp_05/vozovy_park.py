class Vuz:
    def __init__(self, jmeno, kapacita):
        self.jmeno = jmeno
        self.kapacita = kapacita

    def __repr__(self):
        return f'{self.jmeno}: {self.kapacita}'


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


vozovy_park = [
    Vuz(jmeno='vuz1', kapacita=45),
    Vuz(jmeno='vuz2', kapacita=30),
    Vuz(jmeno='vuz3', kapacita=25),
    Vuz(jmeno='vuz4', kapacita=20),
    Vuz(jmeno='vuz5', kapacita=10),
    Vuz(jmeno='vuz6', kapacita=9),
    Vuz(jmeno='vuz7', kapacita=5)
]

print(vozovy_park)
print(secti_celkovou_kapacitu(vozovy_park))
print(najdi_podle_kapacity(vozovy_park, 15))
