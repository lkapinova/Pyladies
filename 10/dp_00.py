class CeleCislo:

    def __init__(self, hodnota):
        self.hodnota = hodnota

    def secti(self, cislo):
        return CeleCislo(self.hodnota + cislo.hodnota)

    def odecti(self, cislo):
        return CeleCislo(self.hodnota - cislo.hodnota)

    def vynasob(self, cislo):
        return CeleCislo(self.hodnota * cislo.hodnota)

    def vydel(self, cislo):
        return CeleCislo(self.hodnota // cislo.hodnota)
    
    def __add__(self, other):
        return self.secti(other)

    def __sub__(self, other):
        return self.odecti(other)
    
    def __mul__(self, other):
        return self.vynasob(other)
    
    def __truediv__(self, other):
        return self.vydel(other)

    # vracim cele cislo pro konzistenci
    def porovnej(self, cislo):
        if self.hodnota < cislo.hodnota:
            return CeleCislo(-1)
        elif self.hodnota > cislo.hodnota:
            return CeleCislo(1)
        else:
            return CeleCislo(0)

    def je_sude(self):
        if self.hodnota % 2 == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f"CeleCislo({self.hodnota})"


jedna = CeleCislo(1)
dva = CeleCislo(2)
tri = CeleCislo(3)
sedm = CeleCislo(7)
dvanact = CeleCislo(12)

x = sedm + dvanact - dva
print(x)

print(sedm.secti(dva).je_sude())
print(sedm.secti(dvanact))
print(sedm / dva)
print(sedm * tri)
print(sedm.odecti(jedna))
print(sedm.porovnej(dvanact))
print(dvanact.porovnej(tri))
print(dvanact.je_sude())

