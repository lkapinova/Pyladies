# Napiš funkci, která převede římské číslice na číslo (int).

M = 1000
CM = 900
D = 500
CD = 400
C = 100
XC = 90
L = 50
XL = 40
X = 10
IX = 9
V = 5
IV = 4
I = 1

rimska_soustava = ['M','CM','D','CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
arabska_soustava = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

rimske_cislo = list("MCMLXXXII")
arabske_cislo = 0
print(rimske_cislo)

for i in rimske_cislo:
    if i == "M":
        arabske_cislo = arabske_cislo + M

print(arabske_cislo)