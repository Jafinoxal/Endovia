# -*- coding: utf-8 -*-
# Endovia (Rocks)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 30,
    1: 30,
    2: 30,
    3: 30,
    4: 30,
    5: 30,
    6: 30,
    7: 30,
    8: 30,
    9: 30,
    10: 30,
    11: 30,
    12: 30,
    13: 30,
    14: 30,
    15: 30,
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
    15: 15,
    }

def _name():
    return {
    0: "Talc Rock",
    1: "Quartz Rock",
    2: "Bari Rock",
    3: "Celest Rock",
    4: "Rhodo Rock",
    5: "Azur Rock",
    6: "Malac Rock",
    7: "Calcium Rock",
    8: "Magnet Rock",
    9: "Hali Rock",
    10: "Flouri Rock",
    11: "Graphite Rock",
    12: "Chalk Rock",
    13: "Sulphur Rock",
    14: "Marble Rock",
    15: "Granite Rock",
    }

def _kind():
    return {
    0: "Rock",
    1: "Rock",
    2: "Rock",
    3: "Rock",
    4: "Rock",
    5: "Rock",
    6: "Rock",
    7: "Rock",
    8: "Rock",
    9: "Rock",
    10: "Rock",
    11: "Rock",
    12: "Rock",
    13: "Rock",
    14: "Rock",
    15: "Rock",
    }

def _description():
    return {
    0: "A mineral deposit is in this.",
    1: "A mineral deposit is in this.",
    2: "A mineral deposit is in this.",
    3: "A mineral deposit is in this.",
    4: "A mineral deposit is in this.",
    5: "A mineral deposit is in this.",
    6: "A mineral deposit is in this.",
    7: "A mineral deposit is in this.",
    8: "A mineral deposit is in this.",
    9: "A mineral deposit is in this.",
    10: "A mineral deposit is in this.",
    11: "A mineral deposit is in this.",
    12: "A mineral deposit is in this.",
    13: "A mineral deposit is in this.",
    14: "A mineral deposit is in this.",
    15: "A mineral deposit is in this.",
    }

def _symbol(): # 6.
    return {
    0: "\x12",
    1: "\x12",
    2: "\x12",
    3: "\x12",
    4: "\x12",
    5: "\x12",
    6: "\x12",
    7: "\x12",
    8: "\x12",
    9: "\x12",
    10: "\x12",
    11: "\x12",
    12: "\x12",
    13: "\x12",
    14: "\x12",
    15: "\x12",
    }

def _color():
    return {
    0: (63,63,63, (0,0,0)),
    1: ((127,127,127), (0,0,0)),
    2: ((63,63,63), (0,0,0)),
    3: ((63,63,63), (0,0,0)),
    4: ((127,127,127), (0,0,0)),
    5: ((191,191,191), (0,0,0)),
    6: ((63,63,63), (0,0,0)),
    7: ((191,191,191), (0,0,0)),
    8: ((127,127,127), (0,0,0)),
    9: ((127,127,127), (0,0,0)),
    10: ((191,191,191), (0,0,0)),
    11: ((63,63,63), (0,0,0)),
    12: ((63,63,63), (0,0,0)),
    13: ((63,63,63), (0,0,0)),
    14: ((191,191,191), (0,0,0)),
    15: ((191,191,191), (0,0,0)),
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
    15: True,
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
    15: False,
    }


def rocks():
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
    15: (_category()[15], _identity()[15], _name()[15], _kind()[15], _description()[15], _symbol()[15], _color()[15], _clip()[15], _transparent()[15]),
    }

# Jafinoxal.
