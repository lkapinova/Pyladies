# Napis funkci, ktera dostane seznam celych cisel a vrati novy seznam,
# ktery obsahuje jen ta cisla, ktera jsou kladna

import random


def seznam_kladnych_cisel(seznam):

    kladna_cisla = []

    for cislo in seznam:
        if cislo >= 0:
            kladna_cisla.append(cislo)

    return kladna_cisla


muj_seznam = random.sample(range(-100, 100), 30)
print(muj_seznam)
print(seznam_kladnych_cisel(muj_seznam))
