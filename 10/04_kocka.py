class Kocka:

    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocet_zivotu = 9

    def zamnoukej(self):
        self.uber_zivot()
        if self.je_ziva():
            return 'Mnau!'
        else:
            return 'mrtva kocka'
    
    def je_ziva(self):
        if self.pocet_zivotu > 0:
            return True
        else:
            return False
    
    def uber_zivot(self):
        self.pocet_zivotu -= 1
        return self.pocet_zivotu
    
    def snez(self, jidlo):
        if jidlo == 'ryba':
            if self.pocet_zivotu < 0 and self.pocet_zivotu > 9:
                self.pocet_zivotu += 1
        # return "Snedla jsem {}.".format(jidlo)
        return f'Snedla jsem {jidlo}, mam {self.pocet_zivotu} zivotu.'

moje_kocka = Kocka("Micka")
print(moje_kocka.zamnoukej())
print(moje_kocka.je_ziva())
print(moje_kocka.uber_zivot())
print(moje_kocka.snez("mleko"))
print(moje_kocka.snez('ryba'))
print(moje_kocka.zamnoukej())
print(moje_kocka.pocet_zivotu)
print(moje_kocka.zamnoukej())
print(moje_kocka.pocet_zivotu)
print(moje_kocka.zamnoukej())
