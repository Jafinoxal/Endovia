# -*- coding: utf-8 -*-
# Endovia (Exits)
# Copyright (C) 2010-2020 Jeremy Aaron Flexer.

def _category():
    return {
    0: 42,
    1: 42,
    2: 42,
    3: 42,
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
    0: "Upwards Stairs",
    1: "Downwards Stairs",
    2: "Upwards Ladder",
    3: "Downwards Ladder"
    }

def _kind():
    return {
    0: "Exit",
    1: "Exit",
    2: "Exit",
    3: "Exit",
    }

def _description():
    return {
    0: "This goes up.",
    1: "This goes down.",
    2: "This goes up.",
    3: "This goes down."
    }

def _symbol(): # 24/25.
    return {
    0: "\x18",
    1: "\x19",
    2: "\x18",
    3: "\x19"
    }

def _color():
    return {
    0: ((95,95,95), (0,0,0)),
    1: ((95,95,95), (0,0,0)),
    2: ((95,95,95), (0,0,0)),
    3: ((95,95,95), (0,0,0)),
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
    }


def exits():
    return {
    0: (_category()[0], _identity()[0], _name()[0], _kind()[0], _description()[0], _symbol()[0], _color()[0], _clip()[0], _transparent()[0]),
    1: (_category()[1], _identity()[1], _name()[1], _kind()[1], _description()[1], _symbol()[1], _color()[1], _clip()[1], _transparent()[1]),
    2: (_category()[2], _identity()[2], _name()[2], _kind()[2], _description()[2], _symbol()[2], _color()[2], _clip()[2], _transparent()[2]),
    3: (_category()[3], _identity()[3], _name()[3], _kind()[3], _description()[3], _symbol()[3], _color()[3], _clip()[3], _transparent()[3]),
}

# Jafinoxal.
