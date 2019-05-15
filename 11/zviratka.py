# class Kotatko():
#     def __init__(self, jmeno):
#         self.jmeno = jmeno
#         self.brisko = "prázdné"

#     def snez(self, jidlo):
#         print("{}: {} mi chutná!".format(self.jmeno, jidlo))
#         self.brisko = "nasycené"

#     def zamnoukej(self):
#         print("{}: Mňau!".format(self.jmeno))


# class Stenatko():
#     def __init__(self, jmeno):
#         self.jmeno = jmeno
#         self.brisko = "prázdné"

#     def snez(self, jidlo):
#         print("{}: {} mi chutná!".format(self.jmeno, jidlo))
#         self.brisko = "nasycené"

#     def zastekej(self):
#         print("{}: Haf!".format(self.jmeno))


# class Kuratko():
#     def __init__(self, jmeno):
#         self.jmeno = jmeno
#         self.brisko = "prázdné"

#     def snez(self, jidlo):
#         print("{}: {} mi chutná!".format(self.jmeno, jidlo))
#         self.brisko = "nasycené"

#     def zapipej(self):
#         print("{}: Píp!".format(self.jmeno))



# Popíšeme jak vypadá obecné "Zvířátko"
class Zviratko():
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.brisko = "prázdné"

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))
        self.brisko = "nasycené"

# A nyní už jen popisujeme, čím se konkrétní zvířátka liší od obecného zvířátka:

# pokud za název nové třídy napíšeme do závorky název jiné třídy,
# tak nová třída z této třídy podědí vše, co nepřeprogramujeme.
class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))


class Kuratko(Zviratko):
    def zapipej(self):
        print("{}: Píp!".format(self.jmeno))


class Velryba(Zviratko):
    def snez(self, jidlo):
        print("{}: {} jsem slupla. Ale hlad mám pořád!".format(self.jmeno, jidlo))
        self.brisko = "polosyté"

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss').replace('S', 'Sss')
        super().__init__(jmeno)

    def zasyc(self):
        print("{}: Ssssss!".format(self.jmeno))

mourek = Kotatko("Mourek")
micka = Kotatko("Micka")
alik = Stenatko("Alík")
erik = Kuratko("Erik")
karlicka = Velryba("Karlička")
stano = Hadatko("Stanislav")

alik.zastekej()
erik.zapipej()
for kote in [mourek, micka]:
    kote.zamnoukej()
stano.zasyc()

zoo = [mourek, micka, alik, erik, karlicka]
menu = ["konzerva", "granulky", "kost", "žížalka", "plankton"]
for zviratko, pokrm in zip(zoo, menu):
    zviratko.snez(pokrm)


# Auto > Volant

# Tvar > Čtverec

# Žák > Třída

# Kurník > Slepička

# Slovník "dict" > Seřazený slovník

# Maso > Vepřové

# Hrací pole > Figurka hráče


