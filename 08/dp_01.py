# Napiš funkci, která vypíše obsah slovníku (klíče a k nim náležící hodnoty) na jednotlivé řádky.

# Funkci, která něco vypisuje, je vhodné pojmenovat speciálně, zde třeba vypis_slovnik,
# aby bylo jasné, že jen vypisuje a nic nevrací. Například:

# >>> vypis_slovnik(mocniny(4))
# Klíč 1, hodnota 1
# Klíč 2, hodnota 4
# Klíč 3, hodnota 9
# Klíč 4, hodnota 16


def mocniny(pocet):
    "Funkce vytvori slovnik cisel a jejich mocnin."

    mocniny = {}

    for i in range(1, pocet+1):
        mocniny[i] = i**2

    return mocniny


def vypis_slovnik(slovnik):
    "Fuknce vypíše po řádcích klíče a hodnoty ze zadaného slovníku."

    for klic, hodnota in slovnik.items():
        print("Klic {}, hodnota {}".format(klic, hodnota))


vypis_slovnik(mocniny(5))
