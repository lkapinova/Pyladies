# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:

# "x" – Vyhrál hráč s křížky (pole obsahuje "xxx")
# "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
# "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

def vyhodnot(piskvorky):
    "Funkce vyhodnotí 1D piškvorky. Pro vítězství jsou nutné tři znaky v řadě."

    if "xxx" in piskvorky:
        vysledek = 'x'
    elif "ooo" in piskvorky:
        vysledek = 'o'
    elif "-" not in piskvorky:
        vysledek = "!"
    else:
        vysledek = '-'
    return vysledek

print(vyhodnot("xxoxoxoxoxxoxxoox"))
print(vyhodnot("xxxoxoxox-xxoxxoo"))
print(vyhodnot("xxoooxoxox-xxoxxoo-o--"))
print(vyhodnot("----x--o--xx--oo-xo-oxo--"))
