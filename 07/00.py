cisla = [1,2,3,4,5,6,7,8,9,10]

# Zamena
# cisla[0] = 42
# cisla[2:5] = [15]
# cisla[0:3] = []

# # Pridani
# cisla = cisla + [11]
# cisla.append(12)
# cisla.append([13,14,15])
# cisla.extend([13,14,15])

# mazani
# cisla[0:3] = []
# del cisla[9]
# cisla.clear()
# cisla.remove(5) # odstrani pouze prvni hodnotu v seznamu

# POP
# posledni = cisla.pop()
# print(posledni)

# razeni
# cisla.sort()
# cisla.sort(reverse=True)

#delka
#len(cisla)

# print(9 in cisla)
# print(9 not in cisla)
# print(cisla.count(9))

# tvorba retezce
# string = 'ABC'
# seznam = list(string)
# seznam = list(range(100))

# rozdeleni stringu
slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
slova1 = 'Tato věta je složitá, rozdělme ji na slova!'.split(',')
print(slova)
print(slova1)

# slozeni seznamu, bude z toho string 
veta = ' '.join(slova)
veta = '-'.join(slova)
print(veta)

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

# promenne
seznamA = [1, 2, 3]
#seznamB = seznamA
seznamB = list(seznamA)

seznamA.append(4)

print(seznamA)
print(seznamB)


# print(cisla)
# print(seznam)