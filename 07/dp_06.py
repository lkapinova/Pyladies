# Napiš funkci, která převede římské číslice na číslo (int).


def prevod_rimskych_cisel(rimske_cislo):
    "Prevadi rimska cisla na arabska."

    rimska_soust_dvojice = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']
    arabska_soust_dvojice = [900, 400, 90, 40, 9, 4]
    rimska_soust = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arabska_soust = [1000, 500, 100, 50, 10, 5, 1]
    vysledek = 0
    

    for i in rimska_soust_dvojice:
        if i in rimske_cislo:
            vysledek += arabska_soust_dvojice[rimska_soust_dvojice.index(i)]
            rimske_cislo = rimske_cislo[:rimske_cislo.index(i)] + rimske_cislo[(rimske_cislo.index(i)+2):]

    for i in rimska_soust:
        vysledek += rimske_cislo.count(i)*arabska_soust[rimska_soust.index(i)]

    return vysledek


print(prevod_rimskych_cisel("MCMLXXXII"))       # 1982
print(prevod_rimskych_cisel("MMXIX"))           # 2019
print(prevod_rimskych_cisel("MDCCLXIII"))       # 1763
print(prevod_rimskych_cisel("MCMXL"))           # 1940
