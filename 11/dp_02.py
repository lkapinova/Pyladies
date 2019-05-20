# Vytvoř funkci, která spočítá celkovou kapacitu všech vozů ve vozovém parku – mohla by vypadat např. takto:

# def secti_celkovou_kapacitu(seznam_vozu):
#     ...


def secti_celkovou_kapacitu(seznam_vozu):
    celkova_kapacita = 0
    for vuz in seznam_vozu:
        celkova_kapacita = celkova_kapacita + vuz.kapacita
    return celkova_kapacita