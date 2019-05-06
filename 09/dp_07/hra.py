from obesenec import hrat_obesence
import random

slova = ["pocestný", "radio", "srdce", "výtažek", "stadion", "květina", "zrcadlo", "klaxon", "kufr", "katr",
         "kabel", "počítadlo", "užovka", "podstavec", "převoz", "krmě", "studio", "azbest", "boule", "pazneht", "magnet"]

while True:

    nova_hra = input("Chceš si zahrát oběšence? Odpovídej ano/ne: \n")

    if nova_hra == "ano":

        hledane_slovo = random.choice(slova)
        hrat_obesence(hledane_slovo)

    elif nova_hra == "ne":

        print("Díky za hru.")
        break

    else:
        print('Nerozumím.')
