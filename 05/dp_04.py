# Napiš funkci tah_hrace, která dostane řetězec s herním polem, 
# zeptá se hráče, na kterou pozici chce hrát, 
# a vrátí herní pole se zaznamenaným tahem hráče. 
# Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. 
# Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.

def tah_hrace(herni_pole):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    while True:
        tvuj_tah = input("Kam chces umistit svuj symbol? ")
        if tvuj_tah.isdigit():
            tvuj_tah = int(tvuj_tah)
            if tvuj_tah >= 0 and tvuj_tah <= 19:
                if herni_pole[tvuj_tah] == '-':
                    herni_pole = herni_pole[:tvuj_tah] + 'x' + herni_pole[(tvuj_tah+1):]
                elif herni_pole[tvuj_tah] != '-':
                    print("Smula, policko uz je zabrane.")
                    continue
            else:
                print("Bohuzel, netrefil ses do herniho pole.")
                continue
        else:
            print("Co delas?! Hrajeme piskovorky! Zkus to znovu.")
            continue
        return herni_pole

print(tah_hrace('-'*20))
