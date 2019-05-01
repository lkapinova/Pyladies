# Vytvorte soubor test_piskvorky.py
# Zakomentujte spusteni piskvorek v souboru s piskvorkami
# Napiste par testu





from piskvorky import tah

def test_tah():
    assert tah(10*'-',7,'x') == '-------x--'
    assert tah(10*'-',0,'x') == 'x---------'
    assert tah(10*'-',9,'x') == '---------x'
    assert tah(10*'-',0,'str') == 'str---------'

def test_tah_mimo_pole():
    try:
        assert tah(10*'-',10,'x')
    except ValueError:
        assert True

# def test_tah_hrace_input_str():
#     assert tvuj_tah == 'avc'