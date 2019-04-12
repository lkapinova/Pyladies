# Napiš funkci, která dostane dva seznamy jmen zvířat a vrátí tři seznamy:

# zvířata, která jsou v obou seznamech současně (průnik množin: první ∩ druhá),
# zvířata, která jsou jen v prvním seznamu (rozdíl množin: první - druhá),
# zvířata, která jsou jen ve druhém seznamu (rozdíl množin: druhá - první).


def porovnani_seznamu(seznam1, seznam2):
    """Funkce porovna dva seznamy a vytvori tri seznamy. 
    Prvni seznam je prunik dvou seznamu, 
    druhy seznam obsahuje prvky uvedené pouze v seznamu1,
    treti seznam obsahuje prvky uvedené pouze v seznamu2."""

    spolecne_prvky = []
    vyhradne_seznam1 = []
    vyhradne_seznam2 = []

    for i in seznam1:
        if i in seznam2:
            spolecne_prvky.append(i)
        else:
            vyhradne_seznam1.append(i)

    for i in seznam2:
        if i not in spolecne_prvky:
            vyhradne_seznam2.append(i)

    return (spolecne_prvky, vyhradne_seznam1, vyhradne_seznam2)


domaci_zvirata = ["pes", "kočka", "králík", "had"]
lesni_zvirata = ["had", "zajíc", "veverka"]

print(porovnani_seznamu(domaci_zvirata, lesni_zvirata))
