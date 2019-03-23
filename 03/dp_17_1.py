import sys
print("Tento program vybere z pěti, tebou zadaných čísel nejmenší.")

# vložení čísel do listu
number_list = []
for i in range (5):
    a = int(input("Zadej číslo: "))
    number_list.append(a)
print(number_list)

# porovnání hodnot s maximální hodnotou celého číslo
# každé číslo menší než max, bude do max vloženo
max = sys.maxsize
for i in range (5):
    if number_list[i] < max:
        max = number_list[i]
print("Nejmenší číslo je ", max)


