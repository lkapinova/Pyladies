# print("Tento program vybere z pěti, tebou zadaných čísel nejmenší.")

# vložení čísel do listu
number_list = []
for i in range (5):
    a = int(input("Zadej číslo: "))
    number_list.append(a)
print(number_list)

# jako nejmenší číslo je zvoleno první uživatelem zvolené číslo
# každé číslo menší než min, bude do min vloženo
min = number_list[0]
for i in range (5):
    if number_list[i] < min:
        min = number_list[i]
print("Nejmenší číslo je ", min)
