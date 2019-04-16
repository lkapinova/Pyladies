# Had byl pyšný na to, že je v abecedě první. Dokud nepřiletěla "andulka".

# Abys hada uklidnila, vytvoř funkci, která zvířata seřadí podle abecedy, ale bude ignorovat první písmeno t.j. vrátí:

# "had",
# "pes",
# "andulka",
# "kočka",
# "králík".
# Postup:

# Máš seznam hodnot, které chceš seřadit podle nějakého klíče. Klíč se dá z každé hodnoty vypočítat.
# Vytvoř seznam dvojic (klíč, hodnota).
# Seřaď tento seznam dvojic – dvojice se řadí nejdřív podle prvního prvku, pak druhého atd.
# Nakonec vytvoř ze seznamu dvojic opět jen seznam hodnot.
# Proč má zrovna had takovéhle výsadní postavení, zjistíš později.


def seradit_podle_2pismene(seznam):

    seznam = []
    seznam_dvojic = []
    for zvire in domaci_zvirata:
        dvojice = (zvire[1], zvire)
        seznam_dvojic.append(dvojice)

    seznam_dvojic.sort()

    for dvojice in seznam_dvojic:
        seznam.append(dvojice[1])

    return seznam


domaci_zvirata = ["pes", "kočka", "králík", "had", "andulka"]
print(seradit_podle_2pismene(domaci_zvirata))
