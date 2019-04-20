# Napiš funkci, která sečte a vrátí sumu všech klíčů a sumu všech hodnot ve slovníku,
# který dostane jako argument. K vyzkoušení můžeš použít slovník z minulé úlohy.
# Například:
# >>> soucet_klicu_a_hodnot(mocniny(4))
# (10, 30)


def mocniny(pocet):
    "Funkce vytvori slovnik cisel a jejich mocnin."

    mocniny = {}

    for i in range(1, pocet+1):
        mocniny[i] = i**2

    return mocniny


def soucet_klicu_a_hodnot(slovnik):
    "Funkce sečte a vrátí sumu všech klicu a sumu vsech hodnot ze zadaneho slovniku."

    suma_klic = 0
    suma_hodnota = 0

    for klic, hodnota in slovnik.items():
        suma_klic += klic
        suma_hodnota += hodnota

    return suma_klic, suma_hodnota


print(soucet_klicu_a_hodnot(mocniny(10)))
print(soucet_klicu_a_hodnot(mocniny(3)))
