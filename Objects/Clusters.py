# -*- coding: utf-8 -*-
# Endovia (Clusters)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 32,
    1: 32,
    2: 32,
    3: 32,
    4: 32,
    5: 32,
    6: 32,
    7: 32,
    8: 32,
    9: 32,
    10: 32,
    11: 32,
    12: 32,
    13: 32,
    14: 32,
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
    0: "Button Cluster",
    1: "Crimini Cluster",
    2: "Portobello Cluster",
    3: "Shiitake Cluster",
    4: "Abalone Cluster",
    5: "Enoki Cluster",
    6: "Girolle Cluster",
    7: "Porcini Cluster",
    8: "Shimeji Cluster",
    9: "Morel Cluster",
    10: "Reishi Cluster",
    11: "Chaga Cluster",
    12: "Cordyceps Cluster",
    13: "Limane Cluster",
    14: "Turtail Cluster",
    }

def _kind():
    return {
    0: "Cluster",
    1: "Cluster",
    2: "Cluster",
    3: "Cluster",
    4: "Cluster",
    5: "Cluster",
    6: "Cluster",
    7: "Cluster",
    8: "Cluster",
    9: "Cluster",
    10: "Cluster",
    11: "Cluster",
    12: "Cluster",
    13: "Cluster",
    14: "Cluster",
    }

def _description():
    return {
    0: "Mushrooms are growing here.",
    1: "Mushrooms are growing here.",
    2: "Mushrooms are growing here.",
    3: "Mushrooms are growing here.",
    4: "Mushrooms are growing here.",
    5: "Mushrooms are growing here.",
    6: "Mushrooms are growing here.",
    7: "Mushrooms are growing here.",
    8: "Mushrooms are growing here.",
    9: "Mushrooms are growing here.",
    10: "Mushrooms are growing here.",
    11: "Mushrooms are growing here.",
    12: "Mushrooms are growing here.",
    13: "Mushrooms are growing here.",
    14: "Mushrooms are growing here.",
    }

def _symbol(): # 29.
    return {
    0: "\x1d",
    1: "\x1d",
    2: "\x1d",
    3: "\x1d",
    4: "\x1d",
    5: "\x1d",
    6: "\x1d",
    7: "\x1d",
    8: "\x1d",
    9: "\x1d",
    10: "\x1d",
    11: "\x1d",
    12: "\x1d",
    13: "\x1d",
    14: "\x1d",
    }

def _color():
    return {
    0: ((95,0,127), (0,0,0)),
    1: ((191,0,255), (0,0,0)),
    2: ((95,0,127), (0,0,0)),
    3: ((95,0,127), (0,0,0)),
    4: ((191,0,255), (0,0,0)),
    5: ((232,165,255), (0,0,0)),
    6: ((95,0,127), (0,0,0)),
    7: ((232,165,255), (0,0,0)),
    8: ((191,0,255), (0,0,0)),
    9: ((191,0,255), (0,0,0)),
    10: ((232,165,255), (0,0,0)),
    11: ((95,0,127), (0,0,0)),
    12: ((95,0,127), (0,0,0)),
    13: ((95,0,127), (0,0,0)),
    14: ((232,165,255), (0,0,0)),
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


def clusters():
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
