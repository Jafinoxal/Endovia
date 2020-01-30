# -*- coding: utf-8 -*-
# Endovia (Fires)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 26,
    1: 26,
    2: 26,
    3: 26,
    4: 26,
    }

def _identity():
    return {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    }

def _name():
    return {
    0: "Fire",
    1: "Unlit Fire",
    2: "Simple Fire",
    3: "Camp Fire",
    4: "Bon Fire",
    }

def _kind():
    return {
    0: "Fire",
    1: "Fire",
    2: "Fire",
    3: "Fire",
    4: "Fire"
    }

def _description():
    return {
    0: "A fire.",
    1: "An until fire, potentially large depending on skill.",
    2: "A small fire.",
    3: "A big fire, toasty!.",
    4: "A large fire, bang on the drums and dance in a circle!"
    }

def _symbol(): # *.
    return {
    0: "*",
    1: "*",
    2: "*",
    3: "*",
    4: "*",
    }

def _color():
    return {
    0: ((255,63,0), (0,0,0)),
    1: ((63,63,63), (0,0,0)),
    2: ((255,63,0), (0,0,0)),
    3: ((255,63,0), (0,0,0)),
    4: ((255,63,0), (0,0,0)),
    }

def _clip():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True
    }

def _transparent():
    return {
    0: True,
    1: True,
    2: True,
    3: True,
    4: True,
    }

def fires():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
    4: (_category()[4], _identity()[4], _name()[4], _kind()[4], _description()[4], _symbol()[4], _color()[4], _clip()[4], _transparent()[4]),
    }

# Jafinoxal.
