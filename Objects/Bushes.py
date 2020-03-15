# -*- coding: utf-8 -*-
# Endovia (Bushes)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 33,
    1: 33,
    2: 33,
    3: 33,
    4: 33,
    5: 33,
    6: 33,
    7: 33,
    8: 33,
    9: 33,
    10: 33,
    11: 33,
    12: 33,
    13: 33,
    14: 33,
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
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    }

def _name():
    return {
    0: "Blueberry Bush",
    1: "Blackberry Bush",
    2: "Strawberry Bush",
    3: "Lingonberry Bush",
    4: "Boysenberry Bush",
    5: "Cranberry Bush",
    6: "Cloudberry Bush",
    7: "Redberry Bush",
    8: "Whiteberry Bush",
    9: "Elderberry Bush",
    10: "Gooseberry Bush",
    11: "Mulberry Bush",
    12: "Juniberry Bush",
    13: "Poisonberry Bush",
    14: "Grapevine Bush",
    }

def _kind():
    return {
    0: "Bush",
    1: "Bush",
    2: "Bush",
    3: "Bush",
    4: "Bush",
    5: "Bush",
    6: "Bush",
    7: "Bush",
    8: "Bush",
    9: "Bush",
    10: "Bush",
    11: "Bush",
    12: "Bush",
    13: "Bush",
    14: "Bush",
    }

def _description():
    return {
    0: "A berry or fruit is growing in this bush.",
    1: "A berry or fruit is growing in this bush.",
    2: "A berry or fruit is growing in this bush.",
    3: "A berry or fruit is growing in this bush.",
    4: "A berry or fruit is growing in this bush.",
    5: "A berry or fruit is growing in this bush.",
    6: "A berry or fruit is growing in this bush.",
    7: "A berry or fruit is growing in this bush.",
    8: "A berry or fruit is growing in this bush.",
    9: "A berry or fruit is growing in this bush.",
    10: "A berry or fruit is growing in this bush.",
    11: "A berry or fruit is growing in this bush.",
    12: "A berry or fruit is growing in this bush.",
    13: "A berry or fruit is growing in this bush.",
    14: "A berry or fruit is growing in this bush.",
    }

def _symbol(): # 6.
    return {
    0: "x1d",
    1: "x1d",
    2: "x1d",
    3: "x1d",
    4: "x1d",
    5: "x1d",
    6: "x1d",
    7: "x1d",
    8: "x1d",
    9: "x1d",
    10: "x1d",
    11: "x1d",
    12: "x1d",
    13: "x1d",
    14: "x1d",
    }

def _color():
    return {
    0: ((127,127,0), (0,0,0)),
    1: ((255,255,0), (0,0,0)),
    2: ((127,127,0), (0,0,0)),
    3: ((127,127,0), (0,0,0)),
    4: ((255,255,0), (0,0,0)),
    5: ((255,255,165), (0,0,0)),
    6: ((127,127,0), (0,0,0)),
    7: ((255,255,165), (0,0,0)),
    8: ((255,255,0), (0,0,0)),
    9: ((255,255,0), (0,0,0)),
    10: ((255,255,165), (0,0,0)),
    11: ((127,127,0), (0,0,0)),
    12: ((127,127,0), (0,0,0)),
    13: ((127,127,0), (0,0,0)),
    14: ((255,255,165), (0,0,0)),
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
    10: True,
    11: True,
    12: True,
    13: True,
    14: True,
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
    7: False,
    8: False,
    9: False,
    10: False,
    11: False,
    12: False,
    13: False,
    14: False,
    }


def bushes():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7]),
    8: (_category()[8], _identity()[8], _name()[8], _kind()[8], _description()[8], _symbol()[8], _color()[8], _clip()[8], _transparent()[8]),
    9: (_category()[9], _identity()[9], _name()[9], _kind()[9], _description()[9], _symbol()[9], _color()[9], _clip()[9], _transparent()[9]),
    10: (_category()[10], _identity()[10], _name()[10], _kind()[10], _description()[10], _symbol()[10], _color()[10], _clip()[10], _transparent()[10]),
    11: (_category()[11], _identity()[11], _name()[11], _kind()[11], _description()[11], _symbol()[11], _color()[11], _clip()[11], _transparent()[11]),
    12: (_category()[12], _identity()[12], _name()[12], _kind()[12], _description()[12], _symbol()[12], _color()[12], _clip()[12], _transparent()[12]),
    13: (_category()[13], _identity()[13], _name()[13], _kind()[13], _description()[13], _symbol()[13], _color()[13], _clip()[13], _transparent()[13]),
    14: (_category()[14], _identity()[14], _name()[14], _kind()[14], _description()[14], _symbol()[14], _color()[14], _clip()[14], _transparent()[14]),
    }

# Jafinoxal.
