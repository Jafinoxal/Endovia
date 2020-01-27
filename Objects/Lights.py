# -*- coding: utf-8 -*-
# Endovia (Lights)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 22,
    1: 22,
    2: 22,
    3: 22,
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
    0: "Light",
    1: "Wall Torch",
    2: "Stand Candle",
    3: "Floor Lamp",
    }

def _kind():
    return {
    0: "Light",
    1: "Light",
    2: "Light",
    3: "Light",
    }

def _description():
    return {
    0: "A light.",
    1: "A torch attached to the wall.",
    2: "A candle sitting on a stand.",
    3: "A tall lamp on the floor.",
    }

def _symbol(): # 215.
    return {
    0: "\xd7",
    1: "\xd7",
    2: "\xd7",
    3: "\xd7",
    }

def _color():
    return {
    0: ((255,127,0), (0,0,0)),
    1: ((255,63,0), (0,0,0)),
    2: ((255,63,0), (0,0,0)),
    3: ((255,255,0), (0,0,0)),
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
    1: False,
    2: True,
    3: True,
    }

def lights():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    }

# Jafinoxal.
