class RodneCislo:

    def __init__(self, rodne_cislo):
        self.hodnota = rodne_cislo

    def __str__(self):
        return self.hodnota

    def zkontroluj_format(self):
        for _ in self.hodnota:
            if _.isalpha():
                return False

        if '/' in self.hodnota:
            divided_rc = self.hodnota.split('/', 1)
            if len(divided_rc[0]) == 6 and len(divided_rc[1]) == 4:
                return True
            else:
                return False
        else:
            return False

    def zkontroluj_delitelnost_11(self):
        self.hodnota = self.hodnota[:6]+self.hodnota[7:]
        if int(self.hodnota) % 11 == 0:
            return True
        else:
            return False

    def vypis_datum_narozeni(self):
        rok = int(self.hodnota[:2])
        if 54 <= rok <= 99:
            rok = 1900 + rok
        else:
            rok = 2000 + rok

        mesic = int(self.hodnota[2:4])
        if int(mesic) > 50:
            mesic = int(mesic) - 50

        den = self.hodnota[4:6]

        return f'{den}.{mesic}.{rok}'

    def zjisti_pohlavi(self):
        mesic = int(self.hodnota[2:4])
        if int(mesic) > 50:
            return 'žena'
        else:
            return 'muž'


rc_1 = RodneCislo('995211/4799')
rc_2 = RodneCislo('000516/9185')
rc_3 = RodneCislo('abcdef/abcd')
print(rc_1.zkontroluj_format())
print(rc_1.zkontroluj_delitelnost_11())
print(rc_1.vypis_datum_narozeni())
print(rc_1.zjisti_pohlavi())
print(rc_2.zkontroluj_format())
print(rc_2.zkontroluj_delitelnost_11())
print(rc_2.vypis_datum_narozeni())
print(rc_2.zjisti_pohlavi())
print(rc_3.zkontroluj_format())
