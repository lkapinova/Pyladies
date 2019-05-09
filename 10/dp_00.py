class CeleCislo:

    def __init__(self, hodnota):
        self.hodnota = hodnota

    def secti(self, cislo):
        return self.hodnota + cislo.hodnota

    def odecti(self, cislo):
        return self.hodnota - cislo.hodnota

    def vynasob(self, cislo):
        return self.hodnota*cislo.hodnota

    def vydel(self, cislo):
        return self.hodnota/cislo.hodnota

    def porovnej(self, cislo):
        if self.hodnota < cislo.hodnota:
            return f'{self.hodnota} < {cislo.hodnota}'
        elif self.hodnota > cislo.hodnota:
            return f'{self.hodnota} > {cislo.hodnota}'
        else:
            return f'{self.hodnota} = {cislo.hodnota}'

    def je_sude(self):
        if self.hodnota % 2 == 0:
            return True
        else:
            return False


jedna = CeleCislo(1)
dva = CeleCislo(2)
tri = CeleCislo(3)
sedm = CeleCislo(7)
dvanact = CeleCislo(12)

print(sedm.je_sude())
print(sedm.secti(dvanact))
print(sedm.vydel(dva))
print(sedm.vynasob(tri))
print(sedm.odecti(jedna))
print(sedm.porovnej(dvanact))
print(dvanact.porovnej(tri))
print(dvanact.je_sude())
