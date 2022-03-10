# -*- coding: utf-8 -*-
# Endovia (Walls)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
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
    }

def _name():
    return {
    0: "Wall",
    1: "Sand Stone Wall",
    2: "Stone Wall",
    3: "Cobble Stone Wall",
    4: "Red Brick Wall",
    5: "Cracked Red Brick Wall",
    6: "Stone Brick Wall",
    7: "Cracked Stone Brick Wall",
    8: "Mossy Stone Brick Wall",
    9: "Tile Wall",
    10: "Cracked Tile Wall",
    11: "Wood Wall",
    12: "Cement Wall",
    13: "Concrete Wall",
    }

def _kind():
    return {
    0: "Wall",
    1: "Wall",
    2: "Wall",
    3: "Wall",
    4: "Wall",
    5: "Wall",
    6: "Wall",
    7: "Wall",
    8: "Wall",
    9: "Wall",
    10: "Wall",
    11: "Wall",
    12: "Wall",
    13: "Wall",
    }

def _description():
    return {
    0: "A wall.",
    1: "A sand stone wall.",
    2: "A stone wall.",
    3: "A cobble stone wall.",
    4: "A red brick wall.",
    5: "A cracked red brick wall.",
    6: "A stone brick wall.",
    7: "A cracked stone brick wall",
    8: "A mossy stone brick wall.",
    9: "A tile wall.",
    10: "A cracked tile wall.",
    11: "A wood wall.",
    12: "A cement wall.",
    13: "A concrete wall.",
    }

def _symbol(): # 219.
    return {
    0: "░",
    1: "▒",
    2: "▓",
    3: "▒",
    4: "░",
    5: "░",
    6: "▓",
    7: "▒",
    8: "▒",
    9: "▒",
    10: "▒",
    11: "░",
    12: "▓",
    13: "▓",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((255,255,191), (255,255,191)),
    2: ((127,127,127), (223,223,223)),
    3: ((127,127,127), (63,63,63)),
    4: ((191,143,0), (63,47,0)),
    5: ((191,143,0), (63,47,0)),
    6: ((223,223,223), (127,127,127)),
    7: ((31,31,31), (127,127,127)),
    8: ((0,255,0), (127,127,127)),
    9: ((255,191,239), (255,0,191)),
    10: ((255,114,219), (255,0,191)),
    11: ((191,191,0), (255,114,149)),
    12: ((95,95,95), (31,31,31)),
    13: ((31,31,31), (95,95,95)),
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
    }


def walls():
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
    }

# Jafinoxal.
