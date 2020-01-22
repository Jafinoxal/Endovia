# -*- coding: utf-8 -*-
# Endovia (Boxes)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 10,
    1: 10,
    2: 10,
    3: 10,
    4: 10,
    5: 10,
    6: 10,
    7: 10,
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
    7: 7,
    }

def _name():
    return {
    0: "Box",
    1: "Empty Box",
    2: "Arrows/Bolts Box",
    3: "Runes Box",
    4: "Food Box",
    5: "Ingredient Box",
    6: "Shiny Box",
    7: "Bread Box",
    }

def _kind():
    return {
    0: "Box",
    1: "Box",
    2: "Box",
    3: "Box",
    4: "Box",
    5: "Box",
    6: "Box",
    7: "Box",
    }

def _description():
    return {
    0: "A box.",
    1: "An empty box.",
    2: "A box of arrows and bolts.",
    3: "A box of runes.",
    4: "A box of food.",
    5: "A box of ingredients.",
    6: "A box of high value.",
    7: "A box of bread.",
    }

def _symbol(): # 245.
    return {
    0: "\xf5",
    1: "\xf5",
    2: "\xf5",
    3: "\xf5",
    4: "\xf5",
    5: "\xf5",
    6: "\xf5",
    7: "\xf5",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((255,255,255), (0,0,0)),
    2: ((255,0,0), (0,0,0)),
    3: ((255,255,0), (0,0,0)),
    4: ((191,255,0), (0,0,0)),
    5: ((0,255,0), (0,0,0)),
    6: ((0,0,255), (0,0,0)),
    7: ((164,43,255), (0,0,0)),
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
    7: True,
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
    7: True,
    }

def boxes():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    }

# Jafinoxal.
