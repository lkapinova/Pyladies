class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return self.jmeno

    def snez(self, jidlo):
        return 'snedla jsem {}. Mnam!'.format(jidlo)


class Kotatko(Zviratko):

    def zamnoukej(self):
        return 'Mnau! Ja jsem kocicka {}.'.format(self.jmeno)


class Stenatko(Zviratko):

    def zastekej(self):
        return 'Haf! Ja jsem pejsek {}.'.format(self.jmeno)


kocka1 = Kotatko(jmeno = 'Micka')
kocka2 = Kotatko(jmeno = "Mourek")
pejsek1 = Stenatko(jmeno = 'ALik')
print(kocka1.zamnoukej())
print(pejsek1.zastekej())
print(kocka1.jmeno)
print(pejsek1.snez(kocka1))
print(kocka1.snez("banan"))
print(kocka1.snez(kocka2))

print(kocka2)
