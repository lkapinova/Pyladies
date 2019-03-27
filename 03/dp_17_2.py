print("Tento program vybere z pěti tebou zadaných čísel nejmenší.")

cislo = int(input("Zadej číslo: "))
min = cislo
for i in range(4):
    dalsi_cislo = int(input("Zadej číslo: "))
    if dalsi_cislo < min:
        min = dalsi_cislo

print("Nejmenší číslo je ", min)




