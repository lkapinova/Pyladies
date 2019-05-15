#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import forward, left, exitonclick, penup, pendown, speed
from math import sqrt

class Ctverec():
    def __init__(self, strana, posunuti_x=0, posunuti_y=0, otoceni=0):
        self.posunuti_x = posunuti_x
        self.posunuti_y = posunuti_y
        self.otoceni = otoceni
        self.a = strana
    
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
    
    def vykresli_ctverec(self):
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


class Trojuhelnik():
    def __init__(self, zakladna, posunuti_x=0, posunuti_y=0, otoceni=0):
        self.posunuti_x = posunuti_x
        self.posunuti_y = posunuti_y
        self.otoceni = otoceni
        self.a = zakladna
    
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
    
    def vykresli_trojuhelnik(self):
        self._na_pozici_kresleni()
        forward(self.a)
        left(90+45)
        forward(self.a*sqrt(2)/2)
        left(90)
        forward(self.a*sqrt(2)/2)
        left(90+45)
        self._zpet_na_pocatek()




#vygenerujeme si vhodné tvary
ctverce = []
trojuhelniky = []
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
    ctverce.append(ctverec)
    trojuhelniky.append(trojuhelnik_1)
    trojuhelniky.append(trojuhelnik_2)
    trojuhelniky.append(trojuhelnik_3)
    trojuhelniky.append(trojuhelnik_4)

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
    for ctverec in ctverce:
        ctverec.vykresli_ctverec()
    for trojuhelnik in trojuhelniky:
        trojuhelnik.vykresli_trojuhelnik()

    for ctverec in ctverce:
        ctverec.pootoc(1)
        ctverec.posun(0.5, 0.5)
    for trojuhelnik in trojuhelniky:
        trojuhelnik.pootoc(1)
        trojuhelnik.posun(0.5, 0.5)

exitonclick()

