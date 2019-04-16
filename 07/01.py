# Napis funkci ktera ze obdrzi na vstupu seznam celych cisel
# a vrati to nejvetsi z nich

# Priklad
# vrat_nejvetsi([1,5,12,3,7]) vrati 12
# vrat_nejvetsi([1,1,3,1,3]) vrati 3

def vrat_nejvetsi(seznam):
    if seznam:
        seznam.sort()
        return seznam[-1]
    else:
        return "seznam je prazdny"

# .sort() seznam zmeni
# nasledujici varianty puvodni seznam nemeni
# dalsi varianta - 
    # max =
    # for cislo in seznam:
# dalsi varianta:
#     seznam.min()
#     seznam.max()
         

def vrat_nejmensi(seznam):
    if seznam:
        seznam.sort()
        return seznam[0]
    else:
        return "seznam je prazdny"

print(vrat_nejvetsi([1,5,12,3,7]))
print(vrat_nejvetsi([1,1,3,1,3]))
print(vrat_nejvetsi([]))
print(vrat_nejmensi([1,5,12,3,7]))
print(vrat_nejmensi([1,1,3,1,3]))
print(vrat_nejvetsi([]))