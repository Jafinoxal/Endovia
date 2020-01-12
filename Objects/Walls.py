# -*- coding: utf-8 -*-
# Endovia (Walls)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def category():
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
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    }

def name():
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

def kind():
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

def description():
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

def symbol():
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
    11: "#",
    12: "#",
    13: "#",
    }

def color():
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
    10: True,
    11: True,
    12: True,
    13: True,
    }

def transparent():
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
    10: (category()[10], identity()[10], name()[10], kind()[10], description()[10], symbol()[10], color()[10], clip()[10], transparent()[10]),
    11: (category()[11], identity()[11], name()[11], kind()[11], description()[11], symbol()[11], color()[11], clip()[11], transparent()[11]),
    12: (category()[12], identity()[12], name()[12], kind()[12], description()[12], symbol()[12], color()[12], clip()[12], transparent()[12]),
    13: (category()[13], identity()[13], name()[13], kind()[13], description()[13], symbol()[13], color()[13], clip()[13], transparent()[13]),
    }

# Jafinoxal.
