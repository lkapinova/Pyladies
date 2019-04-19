# Napiš funkci, která převede římské číslice na číslo (int).


def prevod_rimskych_cisel(rimske_cislo):
    "Prevadi rimska cisla na arabska."

    rimska_soustava = ['CM', 'CD', 'XC', 'XL', 'IX',
                       'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabska_soustava = [900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1]
    arabske_cislo = 0
    index = 0

    while index < len(rimske_cislo):
        for i in rimska_soustava:
            if rimske_cislo.startswith(i, index):
                arabske_cislo = arabske_cislo + \
                    arabska_soustava[rimska_soustava.index(i)]
                index += len(i)
                break

    return arabske_cislo


print(prevod_rimskych_cisel("MCMLXXXII"))       # 1982
print(prevod_rimskych_cisel("MMXIX"))           # 2019
print(prevod_rimskych_cisel("MDCCLXIII"))       # 1763
print(prevod_rimskych_cisel("MCMXL"))           # 1940

