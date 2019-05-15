#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import forward, left, exitonclick, penup, pendown, speed
from math import sqrt

# Vše, co měly Ctverec a Trojuhelnik společné bude ve Tvar!
class Tvar():
    def __init__(self, posunuti_x=0, posunuti_y=0, otoceni=0):
        self.posunuti_x = posunuti_x
        self.posunuti_y = posunuti_y
        self.otoceni = otoceni
    
    def _na_pozici_kresleni(self):
        penup()
        forward(self.posunuti_x)
        left(90)
        forward(self.posunuti_y)
        left(-90)
        left(self.otoceni)
        pendown()
    
    def _zpet_na_pocatek(self):
        penup()
        left(-self.otoceni)
        left(-90)
        forward(self.posunuti_y)
        left(-90)
        forward(self.posunuti_x)
        left(180)
        pendown()
    
    def pootoc(self, uhel):
        self.otoceni += uhel
    
    def posun(self, posunuti_x, posunuti_y):
        self.posunuti_x += posunuti_x
        self.posunuti_y += posunuti_y
    

# To Tvar v závorce říká "co nepřeprogramuješ bude stejné, jako u Tvar":
class Ctverec(Tvar):
    def __init__(self, strana, posunuti_x=0, posunuti_y=0, otoceni=0):
# Společné parametry necháme zpracovat __init__ naprogramovaný ve Tvar
# super() umožní přistoupit k __init__ u Tvar i když je u Ctverec přeprogramovaná
        super().__init__(posunuti_x, posunuti_y, otoceni)
        self.a = strana
        
# vykreslit_ctverec jsme přejmenovali na vykresli.
# To budou mít všechny Tvar společné!
    def vykresli(self):
        self._na_pozici_kresleni()
        forward(self.a)
        left(90)
        forward(self.a)
        left(90)
        forward(self.a)
        left(90)
        forward(self.a)
        left(90)
        self._zpet_na_pocatek()


class Trojuhelnik(Tvar):
    def __init__(self, zakladna, posunuti_x=0, posunuti_y=0, otoceni=0):
        super().__init__(posunuti_x, posunuti_y, otoceni)
        self.a = zakladna
    
    def vykresli(self):
        self._na_pozici_kresleni()
        forward(self.a)
        left(90+45)
        forward(self.a*sqrt(2)/2)
        left(90)
        forward(self.a*sqrt(2)/2)
        left(90+45)
        self._zpet_na_pocatek()


#vygenerujeme si vhodné tvary
tvary = []
for i in range(16):
    a = 40+4*i
    otoceni = 10*i
    posunuti_x = 100+50*i
    posunuti_y = 30+3*i+3*i**2
    ctverec = Ctverec(a, otoceni=10*i, posunuti_x=posunuti_x,
        posunuti_y=posunuti_y)
    trojuhelnik_1 = Trojuhelnik(a, otoceni=10*i, posunuti_x=posunuti_x,
        posunuti_y=posunuti_y+a)
    trojuhelnik_2 = Trojuhelnik(a, otoceni=10*i+90, posunuti_x=posunuti_x,
        posunuti_y=posunuti_y)
    trojuhelnik_3 = Trojuhelnik(a, otoceni=10*i+180, posunuti_x=posunuti_x+a,
        posunuti_y=posunuti_y)
    trojuhelnik_4 = Trojuhelnik(a, otoceni=10*i+270, posunuti_x=posunuti_x+a,
        posunuti_y=posunuti_y+a)
    tvary.append(ctverec)
    tvary.append(trojuhelnik_1)
    tvary.append(trojuhelnik_2)
    tvary.append(trojuhelnik_3)
    tvary.append(trojuhelnik_4)

speed(2000) # Kafíčko pro želvičku!

# posuneme se ke kraji
penup()
left(-90)
forward(400)
left(-90)
forward(400)
left(180)
pendown()


# vsechno vykreslime, pootocime a stale dokola
for _ in range(8):
    for tvar in tvary:
        tvar.vykresli()

    for tvar in tvary:
        tvar.pootoc(1)
        tvar.posun(0.5, 0.5)

exitonclick()


# co se stane, když vytvoříme Tvar a zkusíme ho vykreslit? Je to správně?

