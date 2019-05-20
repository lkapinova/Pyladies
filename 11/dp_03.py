# Uprav program tak, aby vozy ve vozovém parku měly různou kapacitu. 
# Kód v úkolu 0. je jen ukázka, můžeš to udělat klidně i úplně jinak :)

class Vuz:
    def __init__(self, jmeno, kapacita):
        self.jmeno = jmeno
        self.kapacita = kapacita

vozovy_park = [
    Vuz(jmeno = 'vuz1', kapacita = 45),
    Vuz(jmeno = 'vuz2', kapacita = 30),
    Vuz(jmeno = 'vuz3', kapacita = 25),
    Vuz(jmeno = 'vuz4', kapacita = 20),
    Vuz(jmeno = 'vuz5', kapacita = 10),
    Vuz(jmeno = 'vuz6', kapacita = 9),
    Vuz(jmeno = 'vuz7', kapacita = 5)
]