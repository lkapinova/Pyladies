#import pytest
from hrnec import Hrnec


def test_Hrnec_init():
    hrnec = Hrnec("jmeno")
    assert(hrnec.jmeno == "jmeno")
    assert(hrnec.obsah == [])


def test_Hrnec_vloz():
    hrnec = Hrnec("jmeno")
    hrnec.vloz("zelí")
    assert(hrnec.obsah == ["zelí"])
    hrnec.vloz("ocet")
    assert(hrnec.obsah == ["zelí", "ocet"])


def test_Hrnec_vyprazdni():
    hrnec = Hrnec("jmeno")
    hrnec.vloz("zelí")
    hrnec.vloz("rum")
    hrnec.vyprazdni()
    assert(hrnec.obsah == [])


def test_Hrnec_uvar():
    hrnec = Hrnec("jmeno")
    hrnec.vloz("ryba")
    hrnec.vloz("voda")
    hrnec.uvar()
    assert(hrnec.obsah == ["uvařená ryba", "uvařená voda"])


def test_Hrnec_slij():
    prvni = Hrnec("prvni")
    druhy = Hrnec("druhy")
    prvni.vloz("mata")
    prvni.vloz("voda")
    prvni.vloz("cukr")
    druhy.vloz("rum")
    prvni.slij(druhy)
    assert(prvni.obsah == ["mata", "voda", "cukr", "rum"])
    assert(druhy.obsah == [])


def test_Hrnec_kolikrat_pouzit():
    hrnec = Hrnec("ocelovy")
    kelimek = Hrnec("palstovy")
    assert(hrnec.kolikrat_pouzit() == 0)
    assert(kelimek.kolikrat_pouzit() == 0)
    hrnec.vloz("písek")
    kelimek.vloz("voda")
    assert(hrnec.kolikrat_pouzit() == 1)
    for _ in range(1000):
        hrnec.vyprazdni()
        hrnec.vloz("písek")
    assert(hrnec.kolikrat_pouzit() == 2001)
    hrnec.slij(kelimek)
    assert(hrnec.kolikrat_pouzit() == 2002)
    assert(kelimek.kolikrat_pouzit() == 1)
    hrnec.uvar()
    assert(hrnec.kolikrat_pouzit() == 2003)

