# -*- coding: utf-8 -*-
# Endovia (Players)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 2000,
    1: 2000,
    2: 2000,
    3: 2000,
    4: 2000,
    5: 2000,
    6: 2000,
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
    }

def name():
    return
    {
    0: "Human",
    1: "Half Elf",
    2: "Snow Elf",
    3: "Wood Elf",
    4: "Deep Elf",
    5: "High Elf",
    6: "Dark Elf",
    }

def kind():
    return
    {
    0: "Player",
    1: "Player",
    2: "Player",
    3: "Player",
    4: "Player",
    5: "Player",
    6: "Player",
    }

def description():
    return
    {
    0: "A human, hails from various lands, good at most things.",
    1: "A human elf hybrid, harder to produce, affinity for magic.",
    2: "A snow elf, from the north, secretive and can take the cold.",
    3: "A wood elf, from the forests, uses nature as a weapon and tool.",
    4: "A deep elf, from the mountains and caves, stealthy and cunning.",
    5: "A high elf, from the plains, great affinity for magic and dominant.",
    6: "A dark elf, from the volcanic ash lands, pride and high culture.",
    }

def symbol():
    return
    {
    0: u"@",
    1: u"@",
    2: u"@",
    3: u"@",
    4: u"@",
    4: u"@",
    6: u"@",
    }

def color():
    return
    {
    0: ((255,0,0), (0,0,0)),
    1: ((255,127,0), (0,0,0)),
    2: ((255,255,0), (0,0,0)),
    3: ((191,255,0), (0,0,0)),
    4: ((0,255,0), (0,0,0)),
    5: ((0,255,191), (0,0,0)),
    6: ((0,0,255), (0,0,0)),
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
    }

def barrels():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    }

# Jafinoxal.
