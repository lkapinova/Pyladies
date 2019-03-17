rychlost = int(input("Jak rychle jsi se včera vracel domů? Zadej rychlost v km/h.:"))

if rychlost >= 250:
    print("Super, koupil jsi Ferari. To jsem si vždycky přála.")
elif rychlost >= 130:
    print("Po Hradecké se jezdí na slušňáka.")
elif rychlost >= 50:
    print("Nj, ta D1... Příště se řiď heslem: Auta stojí, vlaky jedou. Pozn. neplatí pro České dráhy.")
elif rychlost >= 20:
    print("Tak se ale nediv, když jedeš po jižní spojce.")
elif rychlost >= 12:
    print("Ty fakt ten maraton dáš!?")
elif rychlost >= 6:
    print("Paráda, tak pozdě z práce a přitom pln elánu.")
elif rychlost >= 2:
    print("Vypadá to, že sis dal o pár piv víc, než jsi měl.")
elif rychlost == 0:
    print("Jsem na tebe čekala s večeří..")
else:
    print("Tak přijď dnes, já už se nezlobím.")