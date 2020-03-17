# -*- coding: utf-8 -*-
# Endovia (Alters)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 39,
    1: 39,
    2: 39,
    3: 39,
    4: 39,
    5: 39,
    6: 39,
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
    0: "Peace Alter",
    1: "Chaos Alter",
    2: "Nature Alter",
    3: "Runic Alter",
    4: "Holy Alter",
    5: "Unholy Alter",
    6: "Offering Alter",
    }

def _kind():
    return {
    0: "Alter",
    1: "Alter",
    2: "Alter",
    3: "Alter",
    4: "Alter",
    5: "Alter",
    6: "Alter",
    }

def _description():
    return {
    0: "An alter to peace and justice.",
    1: "An alter to chaos and revenge.",
    2: "An alter to nature and balance.",
    3: "A magical alter to create runes.",
    4: "An alter to grant holy power.",
    5: "An alter to grant unholy power.",
    6: "An alter to offer bones, food, and corpses.",
    }

def _symbol(): # #.
    return {
    0: "#",
    1: "#",
    2: "#",
    3: "#",
    4: "#",
    5: "#",
    6: "#",
    7: "#",
    8: "#",
    9: "#",
    10: "#",
    }

def _color():
    return {
    0: ((0,0,255), (0,0,0)),
    1: ((255,0,0), (0,0,0)),
    2: ((0,255,0), (0,0,0)),
    3: ((255,255,0), (0,0,0)),
    4: ((255,0,127), (0,0,0)),
    5: ((191,0,255), (0,0,0)),
    6: ((127,0,255), (0,0,0)),
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
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    }


def alters():
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
