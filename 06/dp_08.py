# Pokud máš ráda matematiku* a nebojíš se výzvy, načti od uživatele číslo n a:

# Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
# Zjisti, jestli je n prvočíslo.
# Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).
# * t.j. nemáš-li ráda matematiku, nedělej tenhle projekt :)

import math

cislo = int(input("Zadej libovolné číslo větší než 0: "))

def faktorial(cislo):
    nasobek = 1
    for i in range(1,cislo+1):
        nasobek = nasobek*i
    return nasobek


def prvocislo(cislo):
    if cislo == 1:
        print("1 neni prvocislo.")
        
    if cislo < 10:
        a = 0
        for i in range (1, cislo):
            if cislo % i == 0:
                a = a + 1
                if a > 1:
                    print("{} není prvocislo.".format(cislo))
                    break
        if a == 1:
            print("{} je prvocislo.".format(cislo))

    if cislo > 10:
        a = 0
        konec_intervalu = int(math.sqrt(cislo+1))
        for i in range (1, konec_intervalu):
            if cislo % i == 0:
                a = a + 1
                if a > 1:
                    print("{} není prvocislo.".format(cislo))
                    break
        if a == 1:
            print("{} je prvocislo.".format(cislo))

def fibonacci(pocet_clenu):
    a = 0
    b = 1
    for i in range(pocet_clenu):
        clen = a + b
        print(clen,end=' ')
        a = b
        b = clen
        


#print(faktorial(cislo))
#prvocislo(cislo)
fibonacci(cislo)