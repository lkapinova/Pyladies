# Pokud máš ráda matematiku* a nebojíš se výzvy, načti od uživatele číslo n a:

# Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
# Zjisti, jestli je n prvočíslo.
# Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).
# * t.j. nemáš-li ráda matematiku, nedělej tenhle projekt :)

import math


def faktorial(cislo):
    "Vypocte faktorial zadaneho cisla."

    nasobek = 1
    for i in range(1, cislo+1):
        nasobek = nasobek*i
    return nasobek


def je_prvocislo(cislo):
    "Zjisti, zda je ci neni zadane cislo prvocislo."

    delitele = 0
    konec_intervalu = int(math.sqrt(cislo)+1)

    for i in range(2, konec_intervalu):
        if cislo % i == 0:
            delitele = delitele + 1

    if cislo == 2 or (cislo > 2 and delitele == 0):
        print("{} je prvocislo".format(cislo))

    else:
        print("{} neni prvocislo".format(cislo))


def fibonacci(pocet_clenu):
    "Vypise zadany pocet clenu Fibonacciho posloupnosti."

    a = 0
    b = 1
    print(1, end=" ")
    for _ in range(pocet_clenu-1):
        clen = a + b
        a = b
        b = clen
        print(clen, end=" ")


cislo = int(input("Zadej libovolné číslo větší než 0: "))

print(str(cislo)+"!" + " = " + str(faktorial(cislo)))

je_prvocislo(cislo)

print("Prvnich " + str(cislo) + " clenu Fibonacciho posloupnosti je:", end=" ")
fibonacci(cislo)
