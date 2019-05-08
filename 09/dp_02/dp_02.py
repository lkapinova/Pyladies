def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    herni_pole = pole[:cislo_policka] + symbol + pole[(cislo_policka+1):]
    return herni_pole


def tah_hrace(herni_pole, symbol_hrac, tvuj_tah):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    if not tvuj_tah.lstrip('-').isdigit():
        raise TypeError("Nezadal jsi cislo.")
        
    tvuj_tah = int(tvuj_tah)

    if not (0 <= tvuj_tah < len(herni_pole)):
        print("Bohuzel, netrefil ses do herniho pole.")
    
    elif herni_pole[tvuj_tah] != '-':
        print("Smula, policko uz je zabrane.")
    
    else:
        herni_pole = tah(herni_pole, tvuj_tah, symbol_hrac)
    
    return herni_pole


