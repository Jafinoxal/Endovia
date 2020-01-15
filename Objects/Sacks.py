# -*- coding: utf-8 -*-
# Endovia (Sacks)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 12,
    1: 12,
    2: 12,
    3: 12,
    4: 12,
    5: 12,
    6: 12,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    }

def _name():
    return {
    0: "Sack",
    1: "Empty Sack",
    2: "Grain Sack",
    3: "Potato Sack",
    4: "Soap Sack",
    5: "Hay Sack",
    6: "Flour Sack",
    }

def _kind():
    return {
    0: "Sack",
    1: "Sack",
    2: "Sack",
    3: "Sack",
    4: "Sack",
    5: "Sack",
    6: "Sack",
    }

def _description():
    return {
    0: "A sack.",
    1: "An empty sack.",
    2: "A sack of grain.",
    3: "Future applicants for french fries.",
    4: "A sack of soap.",
    5: "A sack of hay.",
    6: "A sack of flour.",
    }

def _symbol():
    return {
    0: u"§",
    1: u"§",
    2: u"§",
    3: u"§",
    4: u"§",
    5: u"§",
    6: u"§",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((54,211,255), (0,0,0)),
    2: ((255,0,0), (0,0,0)),
    3: ((255,153,0), (0,0,0)),
    4: ((191,222,0), (0,0,0)),
    5: ((0,255,0), (0,0,0)),
    6: ((255,44,98), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def sacks():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    }

# Jafinoxal.
