# -*- coding: utf-8 -*-
# Endovia (Chests)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
    return
    {
    0: 7,
    1: 7,
    2: 7,
    3: 7,
    4: 7,
    5: 7,
    6: 7,
    7: 7,
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
    0: "Chest",
    1: "Wood Chest",
    2: "Small Chest",
    3: "Large Chest",
    4: "Armour Chest",
    5: "Weapon Chest",
    6: "Plastic Chest",
    7: "Metal Chest",
    }

def kind():
    return
    {
    0: "Chest",
    1: "Chest",
    2: "Chest",
    3: "Chest",
    4: "Chest",
    5: "Chest",
    6: "Chest",
    7: "Chest",
    }

def description():
    return
    {
    0: "A chest.",
    1: "A wood chest.",
    2: "A small chest.",
    3: "A large chest.",
    4: "A chest of armour.",
    5: "A chest of weapons.",
    6: "A plastic chest.",
    7: "A metal chest.",
    }

def symbol():
    return
    {
    0: u"©",
    1: u"©",
    2: u"©",
    3: u"©",
    4: u"©",
    4: u"©",
    6: u"©",
    7: u"©",
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((63,0,15), (0,0,0)),
    2: ((255,255,255), (0,0,0)),
    3: ((255,255,255), (0,0,0)),
    4: ((255,255,255), (0,0,0)),
    5: ((255,255,255), (0,0,0)),
    6: ((95,95,95), (0,0,0)),
    7: ((191,191,191), (0,0,0)),
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
    7; True,
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

def chests():
    return
    {
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    7: (category()[7], identity()[7], name()[7], kind()[7], description()[7], symbol()[7], color()[7], clip()[7], transparent()[7]),
    }

# Jafinoxal.
