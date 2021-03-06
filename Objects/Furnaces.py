# -*- coding: utf-8 -*-
# Endovia (Furnaces)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 24,
    1: 24,
    2: 24,
    3: 24,
    4: 24,
    5: 24,
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
    0: "Furnace",
    1: "Small Furnace",
    2: "Large Furnace",
    3: "Mould Forge",
    4: "Pottery Forge",
    5: "Master Forge",
    }

def _kind():
    return {
    0: "Furnace",
    1: "Furnace",
    2: "Furnace",
    3: "Furnace",
    4: "Furnace",
    5: "Furnace",
    }

def _description():
    return {
    0: "A furnace.",
    1: "A basic small furnace, needs coal.",
    2: "A basic large furnace, needs coal.",
    3: "A furnace for making jewelery.",
    4: "A furnace for making pottery, with a clay wetter.",
    5: "A forge capable of smelting anything, doesn't need coal.",
    }

def _symbol(): # 215.
    return {
    0: "%",
    1: "%",
    2: "%",
    3: "%",
    4: "%",
    5: "%",
    }

def _color():
    return {
    0: ((63,63,63), (0,0,0)),
    1: ((63,63,63), (0,0,0)),
    2: ((63,63,63), (0,0,0)),
    3: ((191,0,47), (0,0,0)),
    4: ((98,0,47), (0,0,0)),
    5: ((98,0,47), (0,0,0)),
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
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    }

def furnaces():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    }

# Jafinoxal.
