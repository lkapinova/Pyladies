from dp_02 import RodneCislo

vstup = input("Zadej rodne cislo: ")

rc = RodneCislo(vstup)
print(rc.zkotroluj_format())
print(rc.zkotroluj_delitelnost_11())
print(rc.vypis_datum_narozeni())
print(rc.zjisti_pohlavi())
