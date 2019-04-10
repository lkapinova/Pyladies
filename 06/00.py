# soubor = open('00.txt', encoding='utf-8')
# obsah = soubor.read()
# soubor.close()

# print(obsah)

with open('00.txt', encoding='utf-8') as soubor:
    obsah = soubor.read()

print(obsah)