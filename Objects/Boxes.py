# -*- coding: utf-8 -*-
# Endovia (Boxes)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 10,
    1: 10,
    2: 10,
    3: 10,
    4: 10,
    5: 10,
    6: 10,
    7: 10,
    }

def identity():
    return
    {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    }

def name():
    return
    {
    0: "Box",
    1: "Empty Box",
    2: "Arrows/Bolts Box",
    3: "Runes Box",
    4: "Food Box",
    5: "Ingredient Box",
    6: "Shiny Box",
    7: "Bread Box",
    }

def kind():
    return
    {
    0: "Box",
    1: "Box",
    2: "Box",
    3: "Box",
    4: "Box",
    5: "Box",
    6: "Box",
    7: "Box",
    }

def symbol():
    return
    {
    0: u"¬",
    1: u"¬",
    2: u"¬",
    3: u"¬",
    4: u"¬",
    4: u"¬",
    6: u"¬",
    7: u"¬",
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((255,255,255), (0,0,0)),
    2: ((255,0,0), (0,0,0)),
    3: ((255,255,0), (0,0,0)),
    4: ((191,255,0), (0,0,0)),
    5: ((0,255,0), (0,0,0)),
    6: ((0,0,255), (0,0,0)),
    7: ((164,43,255), (0,0,0)),
    }

def clip():
    return
    {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    }

def transparent():
    return
    {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    7: True,
    }

def boxes():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    7: (category()[7], identity()[7], name()[7], kind()[7], symbol()[7], color()[7], clip()[7], transparent()[7]),
    }

# Jafinoxal
