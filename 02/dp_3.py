heslo = 8357

print("Zkus si tipnout heslo.")
print("Pokud se trefíš, získáš tajnou informaci.")
print("Nápověda: zkus kombinaci čísel 3,5,7,8. ")
tip = int(input("Zadej heslo:"))

if tip == heslo:
    print("Trefa! Tajná informace zní: 'Jindřich přijede v neděli.''")
else:
    print("Je mi líto, zadal jsi špatné heslo. Zkus to znovu.")
