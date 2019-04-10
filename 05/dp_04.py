# Napiš funkci tah_hrace, která dostane řetězec s herním polem,
# zeptá se hráče, na kterou pozici chce hrát,
# a vrátí herní pole se zaznamenaným tahem hráče.
# Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka.
# Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.


def tah(pole, cislo_policka, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"

    herni_pole = pole[:cislo_policka] + symbol + pole[(cislo_policka+1):]
    return herni_pole

# def tah_hrace(herni_pole):
#     "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

#     while True:
#         tvuj_tah = input("Kam chces umistit svuj symbol? ")
#         if tvuj_tah.isdigit():
#             tvuj_tah = int(tvuj_tah)
#             if tvuj_tah >= 0 and tvuj_tah <= 19:
#                 if herni_pole[tvuj_tah] == '-':
#                     herni_pole = tah(herni_pole, tvuj_tah, 'x')
#                     break #asi tu neni potreba
#                 else:
#                     print("Smula, policko uz je zabrane.")
#             else:
#                 print("Bohuzel, netrefil ses do herniho pole.")
#         else:
#             print("Co delas?! Hrajeme piskovorky! Zkus to znovu.")
#     return herni_pole


def tah_hrace(herni_pole):
    "Funkce zaznamenava tah hrace do herniho pole a kontroluje vstupni data hrace."

    while True:
        tvuj_tah = input("Kam chces umistit svuj symbol? ")

        if not tvuj_tah.isdigit():
            print("Nezadal jsi cislo.")
            continue

        tvuj_tah = int(tvuj_tah)

        if not (0 <= tvuj_tah < len(herni_pole)):
            print("Bohuzel, netrefil ses do herniho pole.")

        elif herni_pole[tvuj_tah] != '-':
            print("Smula, policko uz je zabrane.")

        else:
            herni_pole = tah(herni_pole, tvuj_tah, 'x')
            break
    return herni_pole

print(tah_hrace('-'*20))
print(tah_hrace("----xx----"))
