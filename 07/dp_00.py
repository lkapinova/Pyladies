# Udělej si seznam domácích zvířat. Budeš ho potřebovat v dalších úlohách. Domácí zvířata známe tato: "pes", "kočka", "králík", "had".

# Napiš funkci, která přebere seznam zvířat a slovo a zjistí, jestli je toto slovo v seznamu.

# „Zjistí“ znamená, že funkce vrátí True nebo False.


def najdi_v_seznamu(seznam, slovo):
    return (slovo in seznam)


domaci_zvirata = ["pes", "kočka", "králík", "had"]

print(najdi_v_seznamu(domaci_zvirata, 'pes'))
print(najdi_v_seznamu(domaci_zvirata, 'liska'))
print(najdi_v_seznamu(domaci_zvirata, 'kocka'))
print(najdi_v_seznamu(domaci_zvirata, 'kočka'))
