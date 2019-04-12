# Napiš funkci, která vrací jména domácích zvířat (ze seznamu zadaného argumentem), která začínají na k.


def pocatecni_pismeno_k(seznam):
    "Tato funkce vybere ze seznamu vsechna slova zacinajici na pismeno k."
    pocatecni_pismeno_k = []
    for slovo in seznam:
        if slovo[0] == 'k':
            pocatecni_pismeno_k.append(slovo)

    return pocatecni_pismeno_k


zvirata = ["pes", "papoušek", "kočka", "rybka", "králík", "had", "12345"]
print(pocatecni_pismeno_k(zvirata))
