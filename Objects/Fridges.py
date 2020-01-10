# -*- coding: utf-8 -*-
# Endovia (Fridges)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 6,
    1: 6,
    2: 6,
    3: 6,
    4: 6,
    }

def identity():
    return
    {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    }

def name():
    return
    {
    0: "Fridge",
    1: "Rusty Fridge",
    2: "Small Fridge",
    3: "Large Fridge",
    4: "Mini Fridge",
    }

def kind():
    return
    {
    0: "Fridge",
    1: "Fridge",
    2: "Fridge",
    3: "Fridge",
    4: "Fridge",
    }

def name():
    return
    {
    0: "A fridge.",
    1: "A rusty fridge.",
    2: "A small fridge.",
    3: "A large fridge.",
    4: "Perfect for beer and snacks.",
    }

def symbol():
    return
    {
    0: u"¶",
    1: u"¶",
    2: u"¶",
    3: u"¶",
    4: u"¶"
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((63,63,63), (0,0,0)),
    2: ((255,255,255), (0,0,0)),
    3: ((255,255,255), (0,0,0)),
    4: ((255,255,255), (0,0,0)),
    }

def clip():
    return
    {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    }

def transparent():
    return
    {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    }

def fridges():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    }

# Jafinoxal.
