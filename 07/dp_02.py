# Napiš funkci, která vrací jména domácích zvířat (ze seznamu zadaného argumentem), která jsou kratší než 5 písmen.


def kratka_slova(seznam):
    "Funkce hledá v seznamu slova, která mají maximálně pět písmen."
    kratka_slova = []
    for slovo in seznam:
        if len(slovo) <= 5:
            kratka_slova.append(slovo)
    return kratka_slova


zvirata = ["pes", "papoušek", "kočička", "rybka", "králíček", "had"]
print(kratka_slova(zvirata))
