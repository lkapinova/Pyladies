# Vytvoř si (prozatím) jednoduchý program, 
# který reprezentuje vozový park fiktivního dopravního podniku 
# - mohl by vypadat nějak takto:

# class Vuz:
#     def __init__(self):
#         self.kapacita = 10

# vozovy_park = [
#     Vuz(),
#     Vuz(),
#     Vuz(),
# ]


class Vuz:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.kapacita = 10

vozovy_park = [
    Vuz(jmeno = 'vuz1'),
    Vuz(jmeno = 'vuz2'),
    Vuz(jmeno = 'vuz3'),
    Vuz(jmeno = 'vuz4'),
    Vuz(jmeno = 'vuz5'),
    Vuz(jmeno = 'vuz6'),
    Vuz(jmeno = 'vuz7')
]