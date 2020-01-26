# -*- coding: utf-8 -*-
# Endovia (Wells)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 21,
    1: 21,
    2: 21,
    3: 21,
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
    0: "Well",
    1: "Stone Well",
    2: "Bucket Well",
    3: "Wishing Well",
    }

def _kind():
    return {
    0: "Well",
    1: "Well",
    2: "Well",
    3: "Well",
    }

def _description():
    return {
    0: "A well.",
    1: "A well made of hard stone.",
    2: "A deep well with a bucket for water.",
    3: "Be careful what you wish for!",
    }

def _symbol(): # 245.
    return {
    0: "\xf5",
    1: "\xf5",
    2: "\xf5",
    3: "\xf5",
    }

def _color():
    return {
    0: ((0,0,255), (0,0,0)),
    1: ((0,0,255), (191,191,191)),
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
    0: True,
    1: True,
    2: True,
    3: True,
    }

def wells():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    }

# Jafinoxal.
