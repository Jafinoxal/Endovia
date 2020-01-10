# Endovia (Barrels)
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
    0: "Barrel",
    1: "Empty Barrel",
    2: "Juice Barrel",
    3: "Beer Barrel",
    4: "Milk Barrel",
    5: "Rotten Food Barrel",
    6: "Flour Barrel",
    }

def kind():
    return
    {
    0: "Barrel",
    1: "Barrel",
    2: "Barrel",
    3: "Barrel",
    4: "Barrel",
    5: "Barrel",
    6: "Barrel",
    }

def symbol():
    return
    {
    0: u"¡",
    1: u"¡",
    2: u"¡",
    3: u"¡",
    4: u"¡",
    4: u"¡",
    6: u"¡",
    }

def color():
    return
    {
    0: ((255,255,255), (0,0,0)),
    1: ((255,255,255), (0,0,0)),
    2: ((255,0,0), (0,0,0)),
    3: ((255,153,0), (0,0,0)),
    4: ((191,222,0), (0,0,0)),
    5: ((0,255,0), (0,0,0)),
    6: ((255,255,255), (0,0,0)),
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
    0: (category()[0], identity()[0], name()[0], kind()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    }

# Jafinoxal
