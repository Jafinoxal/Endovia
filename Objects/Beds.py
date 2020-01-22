# -*- coding: utf-8 -*-
# Endovia (Beds)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 15,
    1: 15,
    2: 15,
    3: 15,
    4: 15,
    5: 15,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    }

def _name():
    return {
    0: "Bed",
    1: "Sleeping Bag Bed",
    2: "Mattress Bed",
    3: "Coffin Bed",
    4: "Luxury Bed",
    5: "Feather Bed",
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
    0: "A bed.",
    1: "A hard bed roll and pillow.",
    2: "A regular bed.",
    3: "A bed fit for vampires.",
    4: "The best bed money can buy.",
    5: "A soft bed roll and pillow filled with feathers.",
    }

def _symbol(): # 15.
    return {
    0: "\x0f",
    1: "\x0f",
    2: "\x0f",
    3: "\x0f",
    4: "\x0f",
    5: "\x0f",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((63,62,15), (0,0,0)),
    2: ((159,244,159), (0,0,0)),
    3: ((127,127,127), (0,0,0)),
    4: ((191,191,191), (0,0,0)),
    5: ((223,223,223), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    5: True,
    }

def beds():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    }

# Jafinoxal.
