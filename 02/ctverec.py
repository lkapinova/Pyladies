# Tento program počítá obvod a obsah čtverce a kruhu.
pi = 3.1415926

a = float(input("Enter size of square/ circle radius in cm: "))

print("Obvod čtverce se stranou", a, "cm je", 4*a, "cm.")
print("Obsah čtverce se stranou", a, "cm je", a*a, "cm2.")
print("Obvod kruhu s poloměrem", a, "cm, je", round(2*pi*a, 2), "cm.")
print("Obsah kruhu s poloměrem", a, "cm, je", round(pi*a*a, 2), "cm2.")
