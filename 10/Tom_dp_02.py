import datetime
import math

class RodneCislo:

    def __init__(self, rodne_cislo):

        if len(rodne_cislo) != 11:
            raise Exception(f"Rodne cislo '{rodne_cislo}' nema delku 11 znaku")
        if rodne_cislo[6] != '/':
            raise Exception(f"Rodne cislo '{rodne_cislo}' neobsahuje lomitko na sedme pozici")
    
        try:
            self.rok = int(rodne_cislo[:2])
            self.mesic = int(rodne_cislo[2:4])
            self.den = int(rodne_cislo[4:6])
            self.sesticisli = int(rodne_cislo[0:6])
            self.ctyrcisli = int(rodne_cislo[7:])
        except ValueError:
            raise Exception(f"Rodne cislo '{rodne_cislo}' obsahuje nepovolene znaky")

        hodnota = 100000000 * self.rok + 1000000 * self.mesic + 10000 * self.den + self.ctyrcisli
        if hodnota % 11 != 0:
            raise Exception(f"Rodne cislo '{hodnota}' neni delitelne jedenacti")

        if self.mesic > 50:
            self.pohlavi = 'F'
        else:
            self.pohlavi = 'M'


    def __str__(self):
        return "{:02d}{:02d}{:02d}/{:04d} ({:s})".format(self.rok,self.mesic,self.den,self.ctyrcisli,self.pohlavi)

    def rok_narozeni(self):
        rok = 1900 + self.rok
        if self.rok < 54:
            rok += 100
        return rok

    def mesic_narozeni(self):
        mesic = self.mesic
        if mesic > 50:
            mesic = mesic - 50
        return mesic

    def den_narozeni(self):
        return self.den

    def datum_narozeni(self):
        return datetime.datetime(self.rok_narozeni(), self.mesic_narozeni(), self.den_narozeni())

    # returns timedelta object https://docs.python.org/3/library/datetime.html#timedelta-objects
    def vek(self):
        return datetime.datetime.now() - self.datum_narozeni()

rc_1 = RodneCislo('006008/0119')
print(rc_1)
print(rc_1.vek().days / 365)
print(rc_1.datum_narozeni())

