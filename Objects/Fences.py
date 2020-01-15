# -*- coding: utf-8 -*-
# Endovia (Fences)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 4,
    1: 4,
    2: 4,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
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
    }

def _name():
    return {
    0: "Fence",
    1: "Short Wood Fence",
    2: "Tall Wood Fence",
    3: "Picket Fence",
    4: "Chain Link Fence",
    5: "Barb Wire Fence",
    6: "ELectric Fence",
    }

def _kind():
    return {
    0: "Fence",
    1: "Fence",
    2: "Fence",
    3: "Fence",
    4: "Fence",
    5: "Fence",
    6: "Fence",
    }

def _description():
    return {
    0: "A fence.",
    1: "A short wood fence.",
    2: "A tall wood fence.",
    3: "Your average neighborhood fence.",
    4: "A chain link fence.",
    5: "Careful, this fence is sharp.",
    6: "Zzzzzt, this fence is shocking!",
    }

def _symbol():
    return {
    0: "-",
    1: "-",
    2: "-",
    3: "-",
    4: "-",
    5: "-",
    6: "-",
    }

def _color():
    return {
    0: ((255,255,255), (0,0,0)),
    1: ((191,0,47), (63,47,0)),
    2: ((191,0,47), (63,47,0)),
    3: ((159,159,159), (223,223,223)),
    4: ((63,63,63), (203,203,203)),
    5: ((63,63,63), (203,203,203)),
    6: ((63,63,63), (203,203,203)),
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
    }

def _transparent():
    return {
    0: False,
    1: True,
    2: False,
    3: True,
    4: True,
    5: True,
    6: True,
    }

def fences():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    5: (_category()[5], _identity()[5], _name()[5], _kind()[5], _description()[5], _symbol()[5], _color()[5], _clip()[5], _transparent()[5]),
    6: (_category()[6], _identity()[6], _name()[6], _kind()[6], _description()[6], _symbol()[6], _color()[6], _clip()[6], _transparent()[6]),
    }

# Jafinoxal.
