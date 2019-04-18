# Napiš funkci, která převede římské číslice na číslo (int).


def prevod_rimskych_cisel(rimske_cislo):
    rimska_soust_dvojice = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
    arabska_soust_dvojice = [900, 400, 90, 40, 9, 4]
    rimska_soust = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabska_soust = [1000, 500, 100, 50, 10, 5, 1]
    cislo1 = 0
    cislo2 = 0

    for i, j in zip(rimska_soust_dvojice, arabska_soust_dvojice):
        if i in rimske_cislo:
            cislo1 += j
            a = rimske_cislo.index(i)
            rimske_cislo = rimske_cislo[:a] + rimske_cislo[(a+2):]

    for i, j in zip(rimska_soust, arabska_soust):
        cislo2 += rimske_cislo.count(i)*j

    return (cislo1+cislo2)


print(prevod_rimskych_cisel("MCMLXXXII"))       # 1982
print(prevod_rimskych_cisel("MMXIX"))           # 2019
print(prevod_rimskych_cisel("MDCCLXIII"))       # 1763
print(prevod_rimskych_cisel("MCMXL"))           # 1940
