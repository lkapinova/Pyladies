from obesenec import hrat_obesence
import random

slova = ["pocestný", "radio", "srdce", "výtažek", "stadion", "květina", "zrcadlo", "klaxon", "kufr", "katr",
         "kabel", "počítadlo", "užovka", "podstavec", "převoz", "krmě", "studio", "azbest", "boule", "pazneht", "magnet"]
random.shuffle(slova)
hledane_slovo = random.choice(slova)

hrat_obesence(hledane_slovo)
