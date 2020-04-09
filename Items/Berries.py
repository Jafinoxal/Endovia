# -*- coding: utf-8 -*-
# Endovia (Berries)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 1010,
    1: 1010,
    2: 1010,
    3: 1010,
    4: 1010,
    5: 1010,
    6: 1010,
    7: 1010,
    8: 1010,
    9: 1010,
    10: 1010,
    11: 1010,
    12: 1010,
    13: 1010,
    14: 1010,
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
    0: "Blueberry",
    1: "Blackberry",
    2: "Strawberry",
    3: "Lingonberry",
    4: "Boysenberry",
    5: "Cranberry",
    6: "Cloudberry",
    7: "Redberry",
    8: "Whiteberry",
    9: "Elderberry",
    10: "Gooseberry",
    11: "Mulberry",
    12: "Juniberry",
    13: "Poisonberry",
    14: "Grape",
    }

def _kind():
    return {
    0: "Berry",
    1: "Berry",
    2: "Berry",
    3: "Berry",
    4: "Berry",
    5: "Berry",
    6: "Berry",
    7: "Berry",
    8: "Berry",
    9: "Berry",
    10: "Berry",
    11: "Berry",
    12: "Berry",
    13: "Berry",
    14: "Berry",
    }

def _description():
    return {
    0: "Can be used in alchemy or cooking.",
    1: "Can be used in alchemy or cooking.",
    2: "Can be used in alchemy or cooking.",
    3: "Can be used in alchemy or cooking.",
    4: "Can be used in alchemy or cooking.",
    5: "Can be used in alchemy or cooking.",
    6: "Can be used in alchemy or cooking.",
    7: "Can be used in alchemy or cooking.",
    8: "Can be used in alchemy or cooking.",
    9: "Can be used in alchemy or cooking.",
    10: "Can be used in alchemy or cooking.",
    11: "Can be used in alchemy or cooking.",
    12: "Can be used in alchemy or cooking.",
    13: "Can be used in alchemy or cooking.",
    14: "Can be used in alchemy, wine making, or cooking.",
    }

def _symbol(): # 215.
    return {
    0: "%",
    1: "%",
    2: "%",
    3: "%",
    4: "%",
    5: "%",
    6: "%",
    7: "%",
    8: "%",
    9: "%",
    10: "%",
    11: "%",
    12: "%",
    13: "%",
    14: "%",
    }

def _color():
    return {
    0: ((127,127,127), (0,0,0)),
    1: ((127,127,127), (0,0,0)),
    2: ((127,127,127), (0,0,0)),
    3: ((127,127,127), (0,0,0)),
    4: ((127,127,127), (0,0,0)),
    5: ((127,127,127), (0,0,0)),
    6: ((127,127,127), (0,0,0)),
    7: ((127,127,127), (0,0,0)),
    8: ((127,127,127), (0,0,0)),
    9: ((127,127,127), (0,0,0)),
    10: ((127,127,127), (0,0,0)),
    11: ((127,127,127), (0,0,0)),
    12: ((127,127,127), (0,0,0)),
    13: ((127,127,127), (0,0,0)),
    14: ((127,127,127), (0,0,0)),
    }

def _clip():
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
    9: True,
    10: True,
    11: True,
    12: True,
    13: True,
    14: True,
    }

def _weight():
    return {
    0: 0.1,
    1: 0.1,
    2: 0.1,
    3: 0.1,
    4: 0.1,
    5: 0.1,
    6: 0.1,
    7: 0.1,
    8: 0.1,
    9: 0.1,
    10: 0.1,
    11: 0.1,
    12: 0.1,
    13: 0.1,
    14: 0.1,
    }

def _value():
    return {
    0: 30,
    1: 98,
    2: 170,
    3: 245,
    4: 315,
    5: 380,
    6: 450,
    7: 513,
    8: 580,
    9: 630,
    10: 698,
    11: 761,
    12: 800,
    13: 876,
    14: 910,
    }

def berries():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0], _weight()[0], _value()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1], _weight()[1], _value()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2], _weight()[2], _value()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3], _weight()[3], _value()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4], _weight()[4], _value()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5], _weight()[5], _value()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6], _weight()[6], _value()[6]),
    7: (_category()[7], _identity()[7], _name()[7], _kind()[7], _description()[7], _symbol()[7], _color()[7], _clip()[7], _transparent()[7], _weight()[7], _value()[7]),
    8: (_category()[8], _identity()[8], _name()[8], _kind()[8], _description()[8], _symbol()[8], _color()[8], _clip()[8], _transparent()[8], _weight()[8], _value()[8]),
    9: (_category()[9], _identity()[9], _name()[9], _kind()[9], _description()[9], _symbol()[9], _color()[9], _clip()[9], _transparent()[9], _weight()[9], _value()[9]),
    10: (_category()[10], _identity()[10], _name()[10], _kind()[10], _description()[10], _symbol()[10], _color()[10], _clip()[10], _transparent()[10], _weight()[10], _value()[10]),
    11: (_category()[11], _identity()[11], _name()[11], _kind()[11], _description()[11], _symbol()[11], _color()[11], _clip()[11], _transparent()[11], _weight()[11], _value()[11]),
    12: (_category()[12], _identity()[12], _name()[12], _kind()[12], _description()[12], _symbol()[12], _color()[12], _clip()[12], _transparent()[12], _weight()[12], _value()[12]),
    13: (_category()[13], _identity()[13], _name()[13], _kind()[13], _description()[13], _symbol()[13], _color()[13], _clip()[13], _transparent()[13], _weight()[13], _value()[13]),
    14: (_category()[14], _identity()[14], _name()[14], _kind()[14], _description()[14], _symbol()[14], _color()[14], _clip()[14], _transparent()[14], _weight()[14], _value()[14]),
    }

# Jafinoxal.
