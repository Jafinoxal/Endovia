# -*- coding: utf-8 -*-
# Endovia (Barrels)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 11,
    1: 11,
    2: 11,
    3: 11,
    4: 11,
    5: 11,
    6: 11,
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
    0: "Barrel",
    1: "Empty Barrel",
    2: "Juice Barrel",
    3: "Beer Barrel",
    4: "Milk Barrel",
    5: "Rotten Food Barrel",
    6: "Flour Barrel",
    }

def _kind():
    return {
    0: "Barrel",
    1: "Barrel",
    2: "Barrel",
    3: "Barrel",
    4: "Barrel",
    5: "Barrel",
    6: "Barrel",
    }

def _description():
    return {
    0: "A barrel.",
    1: "An empty barrel.",
    2: "A barrel full of delicious juice.",
    3: "A barrel full of hardy beer.",
    4: "A barrel full of preserved milk.",
    5: "A smelly barrel full of roten food.",
    6: "A barrel full of flour.",
    }

def _symbol(): # 169.
    return {
    0: "\xa9",
    1: "\xa9",
    2: "\xa9",
    3: "\xa9",
    4: "\xa9",
    5: "\xa9",
    6: "\xa9",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((255,255,255), (0,0,0)),
    2: ((255,0,0), (0,0,0)),
    3: ((255,153,0), (0,0,0)),
    4: ((191,222,0), (0,0,0)),
    5: ((0,255,0), (0,0,0)),
    6: ((255,255,255), (0,0,0)),
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

def barrels():
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
