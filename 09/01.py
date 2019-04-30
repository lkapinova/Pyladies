# Funkce zjisti vek, kontrola, jestli je to cislo, jestli je nezaporne.


def vek():
    while True:
        vek = input("Zadej svuj vek: ")

        if int(vek) < 0:
            raise ValueError("Vek nemuze byt zaporne cislo.")
        if int(vek) > 110:
            raise ValueError("To je velmi nepravdepodobne.")

        try:
            return int(vek)
        except ValueError:
            print('To nebylo číslo! Zkus to znovu.')


vek_uzivatele = vek()
print("Uzivatel zadal vek {}.".format(vek_uzivatele))
