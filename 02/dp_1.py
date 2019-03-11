# Změň program dp_1.py (Povrch a objem krychle o dané straně) tak, aby stranu/poloměr mohl uživatel zadat.

strana = float(input("Zadej délku strany krychle v cm pro výpočet povrchu a objemu: "))

print("Povrch krychle o straně", strana, "cm je", 6*strana*strana, "cm2.")
print("Objem krychle o straně", strana, "cm je", strana**3, "cm3.")
