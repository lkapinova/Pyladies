# Napiš funkci, která převede římské číslice na číslo (int).


def prevod_rimskych_cisel(rimske_cislo):
    rimska_soustava = ['CM', 'CD', 'XC', 'XL', 'IX',
                       'IV', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabska_soustava = [900, 400, 90, 40, 9, 4, 1000, 500, 100, 50, 10, 5, 1]
    arabske_cislo = 0

    while len(rimske_cislo) != 0:
        for i, j in zip(rimska_soustava, arabska_soustava):
            if rimske_cislo.startswith(i):
                arabske_cislo += j
                if len(i) == 2:
                    rimske_cislo = rimske_cislo[2:]
                    break
                else:
                    rimske_cislo = rimske_cislo[1:]
                    break

    return arabske_cislo


print(prevod_rimskych_cisel("MCMLXXXII"))       # 1982
print(prevod_rimskych_cisel("MMXIX"))           # 2019
print(prevod_rimskych_cisel("MDCCLXIII"))       # 1763
print(prevod_rimskych_cisel("MCMXL"))           # 1940
