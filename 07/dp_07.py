# Může seznam obsahovat sám sebe? Zkus co nejjednodušeji udělat takový seznam, aby platilo:

# seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0] == 5

seznam = [5]
for i in range(18):
    seznam = [i,i,i,i,i,seznam]
print(seznam[5])

if (seznam[5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][5][0]) == 5:
    print("Hura!")
