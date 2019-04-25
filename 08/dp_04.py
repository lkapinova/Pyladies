# Úkolem je vytvořit známou skautskou hru „Kdo? S kým? Co dělali?“.
# Hra se hráče zeptá postupně na různé otázky, například „Kdo?“, „S kým?“, „Co dělali?“, „Kde?“, „Kdy?“,
# a nakonec „Proč?“, s tím, že mu umožní na jednu otázku odpovědět vícekrát a všechny odpovědi si uloží.
# Na závěr pak hra z každé sady odpovědí vybere náhodně jednu odpověď a z takto vybraných odpovědí složí větu,
# kterou vypíše uživateli.
# Seznam otázek by mělo být možné změnit v kódu na jednom místě bez zásahu do logiky programu.

import random


def hra_otazky_odpovedi():
    "Funkce se ptá na jednoduché otázky, z odpovědí (na každou otázku může hráč odpovědět vícekrát) složí větu a vypíše ji."

    print("""\n Vítej ve hře Otázky a odpovědi. 
Budu se tě ptát na jednoduché otázky, ty napiš odpověď. 
Odpovědí můžeš vložit víc, odděl je od sebe čárkou např.: Pepa, Marie. 
Já z odpovědí složím větu a vypíšu ti ji.\n""")

    otazky = ["Kdo?", "S kym?", "Co dělali?", "Kde?", "Kdy?", "Proč?"]
    otazky_a_odpovedi = {}
    vysledek = []

    # vytvoreni slovniku z otazek a odpovedi
    for i in otazky:
        odpoved = input("Napiš odpověď/odpovědi na otázku: " + i + ": ")
        odpoved = odpoved.split(',')
        otazky_a_odpovedi[i] = odpoved

    # nahodny vyber odpovedi a spojeni do retezce
    for klic in otazky_a_odpovedi:
        vysledek.append(random.choice(otazky_a_odpovedi[klic]))

    print(' '.join(vysledek))


hra_otazky_odpovedi()
