from dp_02 import RodneCislo

vstup = input("Zadej rodne cislo: ")

rc = RodneCislo(vstup)

if rc.zkontroluj_format():
    print(rc.zkontroluj_delitelnost_11())
    print(rc.vypis_datum_narozeni())
    print(rc.zjisti_pohlavi())
else:
    print("Spatny format rodneho cisla")
