# Napis funkci, ktera:
# - Dostane retezec na vstupu
# - kdyz retezec obsahuje "koala" vrati true
# - v opacnem pripade vrati false
# Bonus: funce nesmi brat v uvahu velikost pismen.
# 'koala' je totez co 'Koala' nebo 'KOALA'
# NAPOVEDDA
# "Ah" in "Ahoj" true
# "ah" not in "Ahoj" true

# def hledam_koalu(retezec):
#     koala = 'koala'
#     j = 0
#     for i in retezec:
#         if i != 'k':
#             j += 1
#         elif i == 'k':
#             podretezec = retezec[j:j+5]
#             # print(i)
#             # print(podretezec)
#             print(koala == podretezec)
#             j += 1
        
# hledam_koalu("tralalakoalatralakoalatralalakoalatralala")


# druhy zpusob:
def hledam_koalu(string):
    print('koala' in string)

hledam_koalu("tralalakoalatralalakoala")