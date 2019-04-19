# Může seznam obsahovat sám sebe? Zkus co nejjednodušeji udělat takový seznam, aby platilo:

# seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0] == 5

# seznam = [5]
# for i in range(18):
#     seznam = [i,i,i,i,i,seznam]
# print(seznam[5])

# if (seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0]) == 5:
#     print("Hura!")


# reseni z Pyladies
seznam =  [ 0, 1, 2, 3, 4,  5]
seznam[5] = seznam      # na místo té pětky tam dáme seznam, což je vlastně odkaz na  sebe sama
seznam[0] = 5           # na začátku má být pětka
if (seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0]) == 5:
    print("Hura!")
print(seznam)