# Pokud máš ráda matematiku* a nebojíš se výzvy, načti od uživatele číslo n a:

# Vypočti faktoriál n! (součin všech celých čísel od 1 do n).
# Zjisti, jestli je n prvočíslo.
# Vypiš prvních n členů Fibonacciho posloupnosti (1, 1, 2, 3, 5, 8, 13, 21, …).
# * t.j. nemáš-li ráda matematiku, nedělej tenhle projekt :)



cislo = int(input("Zadej libovolné číslo větší než 0: "))

def faktorial(cislo):
    nasobek = 1
    for i in range(1,cislo+1):
        nasobek = nasobek*i
    return nasobek


def prvocislo(cislo):
    
        

# print(faktorial(cislo))
print(prvocislo(cislo)) 