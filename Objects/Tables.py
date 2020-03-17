# -*- coding: utf-8 -*-
# Endovia (Tables)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 36,
    1: 36,
    2: 36,
    3: 36,
    4: 36,
    5: 36,
    6: 36,
    7: 36,
    8: 36,
    9: 36,
    10: 36,
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
    }

def _name():
    return {
    0: "Wooden Table",
    1: "Metal Table",
    2: "Stone Table",
    3: "Wooden Coffee Table",
    4: "Metal Coffee Table",
    5: "Glass Coffee Table",
    6: "Wooden End Table",
    7: "Metal End Table",
    8: "Wooden Counter",
    9: "Marble Counter",
    10: "Granite Counter"
    }

def _kind():
    return {
    0: "Table",
    1: "Table",
    2: "Table",
    3: "Table",
    4: "Table",
    5: "Table",
    6: "Table",
    7: "Table",
    8: "Table",
    9: "Table",
    10: "Table",
    }

def _description():
    return {
    0: "Time for supper!",
    1: "Time for supper!",
    2: "Time for supper!",
    3: "Best in front of a couch.",
    4: "Best in front of a couch.",
    5: "Best in front of a couch.",
    6: "Best next to a couch or chair.",
    7: "Best next to a couch or chair.",
    8: "Usually in a kitchen.",
    9: "Usually in a kitchen.",
    10: "Usually in a kitchen.",
    }

def _symbol(): # 8.
    return {
    0: "\x08",
    1: "\x08",
    2: "\x08",
    3: "\x08",
    4: "\x08",
    5: "\x08",
    6: "\x08",
    7: "\x08",
    8: "\x08",
    9: "\x08",
    10: "\x08",
    }

def _color():
    return {
    0: ((127,63,79), (0,0,0)),
    1: ((255,165,165), (0,0,0)),
    2: ((63,63,63), (0,0,0)),
    3: ((127,63,79), (0,0,0)),
    4: ((255,165,165), (0,0,0)),
    5: ((191,239,255), (0,0,0)),
    6: ((127,63,79), (0,0,0)),
    7: ((255,165,165), (0,0,0)),
    8: ((127,63,79), (0,0,0)),
    9: ((63,63,63), (0,0,0)),
    10: ((63,63,63), (0,0,0)),
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
    }


def tables():
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
}

# Jafinoxal.
