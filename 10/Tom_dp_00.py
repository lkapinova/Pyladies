class CeleCislo:

    def __init__(self, hodnota):
        self.hodnota = hodnota

    def scitani(self, jine_cislo):
        if isinstance(jine_cislo, CeleCislo):
            return CeleCislo(self.hodnota + jine_cislo.hodnota)
        if isinstance(jine_cislo, int):
            return CeleCislo(self.hodnota + jine_cislo)
        raise Exception("Invlid type argument, has to be either int or CelaCisla")
    
    def odecitani(self, cislo):
        return self.hodnota - cislo
    
    def nasobeni(self, cislo):
        return self.hodnota*cislo
    
    def deleni(self, cislo):
        return self.hodnota/cislo
    
    def boolean(self, cislo):
        if self.hodnota < cislo:
            return f'{self.hodnota} < {cislo}'
        elif self.hodnota > cislo:
            return f'{self.hodnota} > {cislo}'
        else:
            return f'{self.hodnota} = {cislo}'
    
    def je_sude(self):
        if self.hodnota % 2 == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.hodnota)

    def __add__(self, other):
        return self.scitani(other)

sedm = CeleCislo(7)
dvanact = CeleCislo(12)

print(sedm.je_sude())
print(sedm.scitani(3))
print(sedm.deleni(3))
print(sedm.nasobeni(8))
print(sedm.odecitani(5))
print(sedm.boolean(9))
print(dvanact.boolean(9))
print(dvanact.je_sude())
print(dvanact + 8)




    



