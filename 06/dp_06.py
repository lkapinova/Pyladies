# Napiš program, který se zeptá na 3 čísla a zjistí, jestli je jejich součet větší než 10. 
# Dokážeš to napsat tak, aby funkce input byla v kódu zapsaná jen jednou? ;)

cisla = input("Zadej tri cisla. Oddel je od sebe carkou (napr.: 3,6,7): ")
a,b,c = cisla.split(',')
a = int(a)
b = int(b)
c = int(c)

if a+b+c > 10:
    print("Součet čísel {}, {}, {} je větší než 10.".format(a,b,c))
else:
    print("Součet čísel {}, {}, {} je menší než 10.".format(a,b,c))


# soucet = 0
# for i in range(3):
#     cislo = int(input("Zadej cislo: "))
#     soucet = soucet + cislo

# if soucet > 10:
#     print("Součet čísel je větší než 10.")
# else:
#     print("Součet čísel je menší než 10.")