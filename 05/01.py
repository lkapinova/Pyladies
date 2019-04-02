def zamen(retezec, pozice, znak):
    "Tato funkce vrátí řetězec, který má na dané pozici daný znak."

    print(retezec[:pozice]+znak+retezec[(pozice+1):])

zamen('řetezec',3,'ě')
