from obrazek import nakresli_obesence


def slovo_to_string(hledane_slovo):
    if type(hledane_slovo) != str:
        raise TypeError('nezadal jsi slovo')
    else:
        return '-'*len(hledane_slovo)


def dopln_pismeno(slovo, pismeno, pozice):
    if pozice < 0 or pozice > (len(slovo)-1):
        raise ValueError
    else:
        return slovo[:pozice] + pismeno + slovo[(pozice+1):]


def vyhodnoceni(slovo, spatny_tip):
    if '-' not in slovo:
        return "vyhra"
    elif spatny_tip == 10:
        return "prohra"
    else:
        return "hrajeme dal"


def hrat_obesence(hledane_slovo):

    slovo = slovo_to_string(hledane_slovo)
    spatny_tip = 0

    while True:

        print("Hledáme české slovo (i s interpunkcí).")
        print(slovo)

        # hrac vyhral, pokud ve slove neni zadna pomlcka, viz. funkce vyhodnoceni
        if vyhodnoceni(slovo, spatny_tip) == "vyhra":
            print("Gratuluji! Slovo jsi nasel.")
            break

        # hrac prohrava, pokud 10x netipnul spravne pismeno, viz. funkce vyhodnoceni
        if vyhodnoceni(slovo, spatny_tip) == "prohra":
            print("Smůla. Zkus to znovu.")
            print("Hledané slovo je "+hledane_slovo)
            break

        pismeno = input("Zkus si tipnout, jaké je v něm písmeno: ")

        if pismeno in hledane_slovo:
            slovo = dopln_pismeno(slovo, pismeno, hledane_slovo.index(pismeno))
        else:
            spatny_tip += 1
            print(nakresli_obesence(spatny_tip))
