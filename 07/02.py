# Mate seznam retezcu krestnich jmen
# zaznamy = ['pepa', 'Jiří', 'Ivo', 'jan']

# Nektera jmena zacinaji velkym a jine malym pismenem.

# 1. Napiste funkci ktera vrati seznam prvku, ktere zacinaji malym pismenem
# 2. Napiste funkci ktera vrati seznam prvku, ktere zacinaji velkym pismenem

# napr. vrat_mala_pismena(['pepa', 'Jiří', 'Ivo', 'jan']) => ['pepa', 'jan']
# napr. vrat_velka_pismena(['pepa', 'Jiří', 'Ivo', 'jan']) => ['Jiří', 'Ivo']

# Muzete pouzit funkci retezec.islower() na prvni pismeno retezce

def vrat_mala_pismena(jmena):
    mala_jmena = []
    for i in jmena:
        if i.islower():
            mala_jmena.append(i)
    return mala_jmena

def vrat_velka_pismena(jmena):
    mala_jmena = []
    for i in jmena:
        if i.islower():
            mala_jmena.append(i)
    return mala_jmena

print(vrat_mala_pismena(['pepa', 'Jiří', 'Ivo', 'jan']))
# print(vrat_velka_pismena(['pepa', 'Jiří', 'Ivo', 'jan']))