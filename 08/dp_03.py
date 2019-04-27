# Napiš funkci, která jako argument dostane řetězec a vrátí slovník,
# ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a
# jako hodnoty počty výskytů těchto znaků v řetězci.
# Například:
# >>> pocet_znaku("hello world")
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


def pocet_znaku(string):
    "Funkce vrati slovnik, ve kterem budou jako klice jednotliva pismena/znaky a jako hodnoty pocty opakovani."

    pocty_znaku = {}

    for i in string:
        if i in pocty_znaku:
            continue
        else:
            pocet = string.count(i)
            pocty_znaku[i] = pocet
        
    return pocty_znaku


print(pocet_znaku('''Napiš funkci, která jako argument dostane řetězec a vrátí slovník, 
ve kterém budou jako klíče jednotlivé znaky ze zadaného řetězce a 
jako hodnoty počty výskytů těchto znaků v řetězci.'''))
print(pocet_znaku('blablablablabla'))

