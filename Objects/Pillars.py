# -*- coding: utf-8 -*-
# Endovia (Pillars)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 14,
    1: 14,
    2: 14,
    3: 14,
    4: 14,
    5: 14,
    6: 14,
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
    0: "Pillar",
    1: "Wood Pillar",
    2: "Stone Pillar",
    3: "Metal Pillar",
    4: "Cement Pillar",
    5: "Concrete Pillar",
    6: "Sand Stone Pillar",
    }

def _kind():
    return {
    0: "Pillar",
    1: "Pillar",
    2: "Pillar",
    3: "Pillar",
    4: "Pillar",
    5: "Pillar",
    6: "Pillar",
    }

def _description():
    return {
    0: "A pillar.",
    1: "A basic wood pillar.",
    2: "A rock hard stone pillar.",
    3: "A strong metal pillar.",
    4: "A solid cement pillar.",
    5: "A truly tough concrete pillar.",
    6: "A somewhat strong pillar."
    }

def _symbol(): # 221.
    return {
    0: "\xdd",
    1: "\xdd",
    2: "\xdd",
    3: "\xdd",
    4: "\xdd",
    5: "\xdd",
    6: "\xdd",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,0,15), (0,0,0)),
    2: ((159,159,159), (0,0,0)),
    3: ((127,127,127), (0,0,0)),
    4: ((191,191,191), (0,0,0)),
    5: ((223,223,223), (0,0,0)),
    6: ((255,255,191), (0,0,0)),
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

def pillars():
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
