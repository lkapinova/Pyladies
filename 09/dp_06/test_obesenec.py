import pytest
from obrazek import nakresli_obesence
from obesenec import slovo_to_string, dopln_pismeno, vyhodnoceni, hrat_obesence


def test_slovo_to_string():
    assert slovo_to_string("kometa") == "-"*6
    assert slovo_to_string("popocatepetl") == "-"*12


def test_slovo_to_string_int():
    with pytest.raises(TypeError):
        slovo_to_string(157)


def test_slovo_to_string_prazdny_string():
    assert slovo_to_string("") == ""


def test_dopln_pismeno():
    assert dopln_pismeno("-----", "a", 2) == "--a--"
    assert dopln_pismeno("-----", "a", 0) == "a----"
    assert dopln_pismeno("-----", "a", 4) == "----a"


def test_dopln_pismeno_invalid_input():
    with pytest.raises(ValueError):
        dopln_pismeno("-----", "a", 12)


def test_dopln_pismeno_prazdny_retezec():
    with pytest.raises(ValueError):
        dopln_pismeno("", "a", 5)


def test_vyhodnoceni():
    assert vyhodnoceni("hotovo", 7) == 'vyhra'
    assert vyhodnoceni("---a-e-o-", 10) == 'prohra'
    assert vyhodnoceni("", 0) == 'vyhra'
    assert vyhodnoceni("sko--hotovo", 5) == 'hrajeme dal'
