def pohlavi_podle_prijmeni():
    prijmeni = input('Jaké máš přijmení?: ')
    if prijmeni[-1] == 'á':
        print("Tipuji, že jsi žena.")
    else:
        print('Tipuji, že jsi  muž.')

pohlavi_podle_prijmeni()
