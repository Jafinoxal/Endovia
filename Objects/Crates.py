# -*- coding: utf-8 -*-
# Endovia (Crates)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
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

def identity():
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

def name():
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

def kind():
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

def description():
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

def symbol():
    return {
    0: u"¤",
    1: u"¤",
    2: u"¤",
    3: u"¤",
    4: u"¤",
    5: u"¤",
    6: u"¤",
    7: u"¤",
    8: u"¤",
    9: u"¤",
    }

def color():
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

def clip():
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

def transparent():
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
    0: (category()[0], identity()[0], name()[0], kind()[0], description()[0], symbol()[0], color()[0], clip()[0], transparent()[0]),
    1: (category()[1], identity()[1], name()[1], kind()[1], description()[1], symbol()[1], color()[1], clip()[1], transparent()[1]),
    2: (category()[2], identity()[2], name()[2], kind()[2], description()[2], symbol()[2], color()[2], clip()[2], transparent()[2]),
    3: (category()[3], identity()[3], name()[3], kind()[3], description()[3], symbol()[3], color()[3], clip()[3], transparent()[3]),
    4: (category()[4], identity()[4], name()[4], kind()[4], description()[4], symbol()[4], color()[4], clip()[4], transparent()[4]),
    5: (category()[5], identity()[5], name()[5], kind()[5], description()[5], symbol()[5], color()[5], clip()[5], transparent()[5]),
    6: (category()[6], identity()[6], name()[6], kind()[6], description()[6], symbol()[6], color()[6], clip()[6], transparent()[6]),
    7: (category()[7], identity()[7], name()[7], kind()[7], description()[7], symbol()[7], color()[7], clip()[7], transparent()[7]),
    8: (category()[8], identity()[8], name()[8], kind()[8], description()[8], symbol()[8], color()[8], clip()[8], transparent()[8]),
    9: (category()[9], identity()[9], name()[9], kind()[9], description()[9], symbol()[9], color()[9], clip()[9], transparent()[9]),
    }

# Jafinoxal.
