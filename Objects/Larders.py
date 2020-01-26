# -*- coding: utf-8 -*-
# Endovia (Larders)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 19,
    1: 19,
    2: 19,
    3: 19,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    }

def _name():
    return {
    0: "Larder",
    1: "Kitchen Larder",
    2: "Cooled Larder",
    3: "Non-Parishable Larder",
    }

def _kind():
    return {
    0: "Larder",
    1: "Larder",
    2: "Larder",
    3: "Larder",
    }

def _description():
    return {
    0: "A larder.",
    1: "A larder containing all types of food.",
    2: "A larder for storing goods at a cool temperature.",
    3: "A larder for storing goods that don't go bad.",
    }

def _symbol(): # 9.
    return {
    0: "\x09",
    1: "\x09",
    2: "\x09",
    3: "\x09",
    }

def _color():
    return {
    0: ((0,0,255), (0,0,0)),
    1: ((0,0,255), (0,0,0)),
    2: ((0,0,255), (0,0,0)),
    3: ((0,0,255), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    }

def _transparent():
    return {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    }

def larders():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    }

# Jafinoxal.
