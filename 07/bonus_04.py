# Napis funkci, ktera dostane seznam a vrati True
# pokud obsahuje nejake duplicitni hodnoty, jinak vrati false


def find_duplicates(list):
    "Tato funkce hleda duplicitni hodnoty."
    pocet_prvku = len(list)
    list = set(list)
    pocet_prvku_set = len(list)

    if pocet_prvku == pocet_prvku_set:
        return False
    else:
        return True


a = [1, 3, 5, 7, 2, 5, 8, 13, 21, 34, 55, 89]
b = [15, 16, 17, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(find_duplicates(a))
print(find_duplicates(b))
