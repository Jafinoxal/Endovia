# -*- coding: utf-8 -*-
# Endovia (Crates)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 9,
    1: 9,
    2: 9,
    3: 9,
    4: 9,
    5: 9,
    6: 9,
    7: 9,
    8: 9,
    9: 9,
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
    8: 8,
    9: 9,
    }

def _name():
    return {
    0: "Crate",
    1: "Empty Crate",
    2: "Fruit Crate",
    3: "Vegetable Crate",
    4: "Meat Crate",
    5: "Ration Crate",
    6: "Wine Crate",
    7: "Ingredient Crate",
    8: "Shiny Crate",
    9: "Spice Crate",
    }

def _kind():
    return {
    0: "Crate",
    1: "Crate",
    2: "Crate",
    3: "Crate",
    4: "Crate",
    5: "Crate",
    6: "Crate",
    7: "Crate",
    8: "Crate",
    9: "Crate",
    }

def _description():
    return {
    0: "A crate.",
    1: "An empty crate.",
    2: "A crate of various fruit.",
    3: "A crate of various vegetables.",
    4: "A crate of various meats.",
    5: "A crate of rations.",
    6: "A crate of delicious wine.",
    7: "A crate of ingredients.",
    8: "A crate of high value.",
    9: "A crate of spices.",
    }

def _symbol(): # 167.
    return {
    0: u"\xa7",
    1: u"\xa7",
    2: u"\xa7",
    3: u"\xa7",
    4: u"\xa7",
    5: u"\xa7",
    6: u"\xa7",
    7: u"\xa7",
    8: u"\xa7",
    9: u"\xa7",
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
    7: ((127,0,255), (0,0,0)),
    8: ((255,0,127), (0,0,0)),
    9: ((255,0,63), (0,0,0)),
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
    8: True,
    9: True,
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
    8: True,
    9: True
    }

def crates():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    8: (_category()[8], _identity()[8], _name()[8], _kind()[8], _description()[8], _symbol()[8], _color()[8], _clip()[8], _transparent()[8]),
    9: (_category()[9], _identity()[9], _name()[9], _kind()[9], _description()[9], _symbol()[9], _color()[9], _clip()[9], _transparent()[9]),
    }

# Jafinoxal.
